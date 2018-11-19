from django.shortcuts import render
from .models import Post

# Create your views here.


def post_list(request):
    qs = Post.objects.all()

    return render(request, 'notice/post_list.html', {
        'post_list': qs,
    })


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'notice/post_detail.html', {
        'post': post,
    })

