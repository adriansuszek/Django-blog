from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

#my custom pag
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page') # URL/?page=1,
    page_obj = paginator.get_page(page_number)

    # try:
    #     paginated_post_list = paginator.page(page)
    # except PageNotAnInteger:
    #     paginated_post_list = paginator.page(1)
    # except EmptyPage:
# >>> page2.next_page_number()
# Traceback (most recent call last):
# ...
# EmptyPage: That page contains no results
        # paginated_post_list = paginator.page(paginator.num_pages)


    categories = Category.objects.all()
    context = {
        # 'post_list': post_list,

        'post_list': page_obj,
        'page_obj': page_obj,

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
