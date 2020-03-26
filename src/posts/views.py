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


def post(request, slug):
    post_det = Post.objects.get(slug=slug)
    context = {
        'post': post_det,
    }
    return render(request, 'post.html', context)


def contact(request):
    return render(request, 'contact.html', {})
