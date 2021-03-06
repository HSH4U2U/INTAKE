from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from .models import Product, Comment, Category
from django.db.models import Q, Avg


# Create your views here.
def main_page(request):
    # search 구현
    if "search" in request.GET:
        search_term = request.GET["search"]
        if search_term:
            searched_products = Product.objects.filter(
                Q(product_name__icontains=search_term) |
                Q(product_price__icontains=search_term) |
                Q(category__category_name__icontains=search_term)
            ).distinct()
        ctx = {
            'products': searched_products,
            'search_term': search_term,
        }
        return render(request, 'main_app/category.html', ctx)
    else:
        main_products1 = Product.objects.filter(category__pk=1)  # 밀스라이트 제품만 따옴
        main_products2 = Product.objects.filter(category__pk=2)  # 피로그래밍만 따옴
        ctx = {
            'products1': main_products1,
            'products2': main_products2,
        }
        return render(request, 'main_app/main_page.html', ctx)


def product(request, pk):
    # search 구현
    if "search" in request.GET:
        search_term = request.GET["search"]
        if search_term:
            searched_products = Product.objects.filter(
                Q(product_name__icontains=search_term) |
                Q(product_price__icontains=search_term) |
                Q(category__category_name__icontains=search_term)
            ).distinct()
        ctx = {
            'products': searched_products,
            'search_term': search_term,
        }
        return render(request, 'main_app/category.html', ctx)
    else:
        # 상품별 페이지 생성
        product = get_object_or_404(Product, pk=pk)
        # 카테고리 종류 받아오기
        category = product.category
        # 후기 등록 시스템 구현(상품 보여주는 페이지와 같은 곳에서 보이게 구현함)
        form = CommentForm(request.POST, request.FILES or None)
        if request.method == 'POST':
            # 로그인 되었을 때만 쓸 수 있게 할 생각
            if request.user.is_authenticated:
                if form.is_valid():
                    comment = form.save(commit=False)
                    # 자동으로 author와 product 지정
                    comment.author = request.user
                    comment.product = product
                    comment.save()
                    return redirect(comment)        # 다시 상품 해당 페이지로 가야함
                else:
                    form = CommentForm()
            else:
                return redirect('accounts:login')

    # 댓글 목록 받아오기
    comments = Comment.objects.filter(product__pk=pk)

    ctx = {
        'form': form,
        'product': product,
        'category': category,
        'comments': comments,
    }
    return render(request, 'main_app/product.html', ctx)


def category(request, pk):   # 여기서 pk는 category의 pk
    # search 구현
    if "search" in request.GET:
        search_term = request.GET["search"]
        if search_term:
            searched_products = Product.objects.filter(
                Q(product_name__icontains=search_term) |
                Q(product_price__icontains=search_term) |
                Q(category__category_name__icontains=search_term)
            ).distinct()
        ctx = {
            'products': searched_products,
            'search_term': search_term,
        }
        return render(request, 'main_app/category.html', ctx)
    else:
        # 해당 카테고리의 상품 받아오기
        products = Product.objects.filter(category__pk=pk)
        # 해당 카테고리 받아오기
        category = products[0].category

        # sort 구현
        sort_option = "최신 상품순"
        if "sort" in request.GET:
            sort_option = request.GET["sort"]
            if sort_option == "최신 상품순":
                sorted_products = products
            elif sort_option == "댓글 수":
                sorted_products = sorted(products, key=lambda x: x.comment_set.count(), reverse=True)
            elif sort_option == "상품평순":
                sorted_products = sorted(products,
                                         key=lambda x: x.comment_set.all().aggregate(Avg('star'))['star__avg'],
                                         reverse=True)                # aggregate로 필드 내 요소들에 접근 가능!
            elif sort_option == "낮은 가격순":
                sorted_products = sorted(products, key=lambda x: x.product_price)
            elif sort_option == "높은 가격순":
                sorted_products = sorted(products, key=lambda x: x.product_price, reverse=True)
            # else:
            #     sorted_products = Product.objects.filter(category__pk=pk)
            ctx = {
                'products': sorted_products,
                'sort_option': sort_option,
                'category': category,
            }
            return render(request, 'main_app/category.html', ctx)
        else:
            ctx = {
                'products': products,
                'sort_option': sort_option,
                'category': category,
            }
            return render(request, 'main_app/category.html', ctx)


def category_main(request):
    # 카테고리 목록 받아오기
    categorys = Category.objects.all()
    ctx = {
        'categorys': categorys,
    }
    return render(request, 'main_app/category_main.html', ctx)