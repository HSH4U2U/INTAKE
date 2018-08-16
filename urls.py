from django.urls import path, re_path
from.import views


urlpatterns =[
       path('new/', views.post_new),
      #path('new/', views.post_new),
]