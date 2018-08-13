from django.urls import path, re_path, include
from . import views

app_name = "main_app"

urlpatterns = [
    re_path(r'^$', views.main_page, name="main_page"),
    path('product<int:pk>', views.product, name="product"),
]