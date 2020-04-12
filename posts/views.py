from django.shortcuts import render
from .models import Category, Post

def index(request):
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'latest': latest #latest to jest moja lista 3 elementowa i w index.html mamy do niej dostęp, bo przekazaliśmy ją niżej
    }
    return render(request, 'index.html', context) # w TEJ LINIJCE!


def blog(request):
    post_list = Post.objects.order_by('-timestamp')
    last_post_list = post_list[:3]
    categories = Category.objects.all()
    context = {
        'post_list': post_list,
        'last_post': last_post_list,
        'categories': categories
    }
    return render(request, 'blog.html', context)

def last_post(request):
    last_post = Post.objects.order_by('-timestamp')[:1]
    context = {
        'last_post': last_post,
    }
    return render(request, 'post.html', context)

def post(request, slug):
    post_det = Post.objects.get(slug=slug)
    last_post_widget = Post.objects.order_by('-timestamp')[:3]

    context = {
        'post': post_det,
        'last_post_widget': last_post_widget

    }
    return render(request, 'post.html', context)


def contact(request):
    return render(request, 'contact.html', {})
