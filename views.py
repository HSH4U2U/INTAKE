from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from .models import Post


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post()
            post.name = form.cleaned_data['name']
            post.email = form.cleaned_data['email']
            post.phone_number = form.cleaned_data['phone_number']
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.profile = form.cleaned_data['profile']
            post.save()
            return redirect('/ask/new/')
    else:
        form = PostForm()
    return render(request, 'ask/post_form.html', {
        'form': form,
    })

