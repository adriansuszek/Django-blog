from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Category, Post, Comment
from .forms import CommentForm

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
    # post_det = Post.objects.get(slug=slug)
    post_det = get_object_or_404(Post,slug=slug)
    last_post_widget = Post.objects.order_by('-timestamp')[:3]

    form = CommentForm(request.POST or None) #it stands for COMMENT feature
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user #it will be fetched from Comment class from models.py
            form.instance.post = post_det
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'slug': post_det.slug
            }))

    context = {
        'post': post_det,
        'last_post_widget': last_post_widget,
        'form': form,
    }
    return render(request, 'post.html', context)


def contact(request):
    return render(request, 'contact.html', {})
