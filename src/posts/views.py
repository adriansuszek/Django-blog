from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def contact(request):
    return render(request, 'contact.html', {})
