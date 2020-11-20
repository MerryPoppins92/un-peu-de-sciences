from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
	blogs = Blog.objects.order_by('-date')
	return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, the_slug):
	blog = get_object_or_404(Blog, slug = the_slug)
	return render(request, 'blog/detail.html', {'blog':blog})
