from django.shortcuts import render
from .models import Post

def index(request):
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'latest': latest #latest to jest moja lista 3 elementowa i w index.html mamy do niej dostęp, bo przekazaliśmy ją niżej
    }
    return render(request, 'index.html', context) # w TEJ LINIJCE!


def blog(request):
    post_list = Post.objects.order_by('-timestamp')
    context = {
        'post_list': post_list
    }
    return render(request, 'blog.html', context)


def contact(request):
    return render(request, 'contact.html', {})
