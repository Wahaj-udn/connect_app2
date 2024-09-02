from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')

def explore(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'explore.html', {'posts': page_obj})
