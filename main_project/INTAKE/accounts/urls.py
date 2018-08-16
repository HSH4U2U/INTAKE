from django.urls import path, re_path, include
from . import views
from django.conf import settings

app_name = "accounts"

urlpatterns = [
    # path('profile/', views.profile, name="profile"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name="login"),
    path('logout/', views.view_logout, name="logout"),
    path('profile/', views.profile, name='profile'),
]
