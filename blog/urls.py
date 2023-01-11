from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.bl_home, name='bl_home'),
    path('<int:blog_id>/', views.detail, name='detail'),
]