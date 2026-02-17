from django.shortcuts import render, get_object_or_404
from blogs.models import Category, Blog, About

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True,status='Published').order_by('created_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    
    try:
        about = About.objects.get()

    except:
        about = None

    context = {
        'featured_posts' : featured_posts,
        'posts':posts,
        'about':about

    }
    return render(request,'home.html',context)