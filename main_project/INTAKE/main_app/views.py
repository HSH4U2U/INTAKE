from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from .models import Product, Comment


# Create your views here.
# def main_page(request):
#     return render(request, 'main_app/main_page.html')

def main_page(request):
    ctx = {}
    main_products = []
    for pk in range(1, Product.objects.count() + 1):
        main_product = get_object_or_404(Product, pk=pk)
        main_products.append(main_product)
        ctx['product'+str(pk)] = main_products[pk-1]
    return render(request, 'main_app/main_page.html', ctx)


#main_page에서 자동 상품 보이기 구현
# def main_page(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     ctx = {
#         'product': product,
#     }
#     return render(request, 'main_app/main_page.html', ctx)


def product(request, pk):
    # 상품별 페이지 생성
    product = get_object_or_404(Product, pk=pk)

    # 후기 등록 시스템 구현(상품 보여주는 페이지와 같은 곳에서 보이게 구현함)
    form = CommentForm(request.POST, request.FILES)
    if request.method == 'POST':

        # 자동으로 author와 product 지정
        # form.author = request.user
        # form.product = product

        # 로그인 되었을 때만 쓸 수 있게 할 생각
        if request.user.is_authenticated:
            if form.is_valid():
                comment = form.save()
                return redirect(comment)        #다시 상품 해당 페이지로 가야함
            else:
                form = CommentForm()
        else:
            return redirect('accounts:login')
    # 댓글 목록 받아오기
    comments = Comment.objects.filter(product__pk=pk)
    # 여기 아래 아마도 상품 정보랑 html 연결 구현
    ctx = {
        'form': form,
        'product': product,
        'comments': comments,
    }
    return render(request, 'main_app/product.html', ctx)

