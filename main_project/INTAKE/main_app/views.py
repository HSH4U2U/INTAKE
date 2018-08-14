from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from .models import Product
from django.contrib.auth.decorators import permission_required


# Create your views here.
def main_page(request):
    return render(request, 'main_app/main_page.html')


def product(request, pk):
    # 상품별 페이지 생성
    product = get_object_or_404(Product, pk=pk)

    # 후기 등록 시스템 구현(상품 보여주는 페이지와 같은 곳에서 보이게 구현함)
    form = CommentForm(request.POST, request.FILES)
    if request.method == 'POST':
        # 로그인 되었을 때만 쓸 수 있게 할 생각
        # test = permission_required(perm, login_url=None, raise_exception=False)
        # if test is True:        # 위에 perm만 이해하면 될 듯
            if form.is_valid():
                comment = form.save()

                # comment.author = request.user
                # comment.product = product

                return redirect(comment)
            else:
                form = CommentForm()
        # else:
        #     form = CommentForm()

    # 여기 아래 아마도 상품 정보랑 html 연결 구현
    ctx = {
        'form': form,
        'product': product,
    }
    return render(request, 'main_app/product.html', ctx)

