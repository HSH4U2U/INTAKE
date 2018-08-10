from django.urls import path, re_path, include
from . import views

app_name = "main_app"

urlpatterns = [
    re_path(r'^$', views.main_page, name="main_page"),
    re_path(r'^product/$', views.product_detail, name="product_detail"),
]