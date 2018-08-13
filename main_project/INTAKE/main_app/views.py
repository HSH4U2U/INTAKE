from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment


# Create your views here.
def main_page(request):
    return render(request, 'main_app/main_page.html')


def product(request):
    # 후기 시스템 구현
    form = CommentForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save()
            return redirect(comment)
    else:
        form = CommentForm()

    # 여기 아래 아마도 상품 정보랑 html 연결 구현
    ctx = {
        'form': form,
    }
    return render(request, 'main_app/product.html', ctx)

