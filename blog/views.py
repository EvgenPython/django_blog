from django.shortcuts import render, get_object_or_404
from .models import BlogProject

def bl_home(request):
    blog_project = BlogProject.objects.order_by('-data')[:5]
    return render(request, 'bl/bl_home.html', {'blog_project': blog_project})

def detail(request, blog_id):
    blog = get_object_or_404(BlogProject, pk=blog_id)
    return render(request, 'bl/detail.html', {'blog': blog})