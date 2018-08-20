from django.urls import path
from INTAKE_repo.cs_center import views

urlpatterns =[
       path('new/', views.post_new),
      #path('new/', views.post_new),
]