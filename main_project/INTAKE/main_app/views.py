from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from .models import Comment, Product


# Create your views here.
def main_page(request):
    return render(request, 'main_app/main_page.html')


def product(request, pk):
    # 상품별 페이지 생성
    product = get_object_or_404(Product, pk=pk)

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
        'product': product,
    }
    return render(request, 'main_app/product.html', ctx)

