from django.urls import path

from orm_test import views

app_name = "main"

urlpatterns = [
    path('', views.main_page, name="home"),
    path('posts/', views.posts_view, name="posts"),
    path('post/detail/<int:post_id>/', views.post_detail, name="post_detail"),
]