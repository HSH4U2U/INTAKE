from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'main_app/main_page.html')


def product_detail(request):
    return render(request, 'main_app/product_detail.html')



