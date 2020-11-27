from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.BlogPostListView.as_view(), name='blogposts'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogs/<int:pk>', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('bloggers/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('blogs/<int:pk>/create', views.blogpost_add_comment, name='blogpost-comment'),
]
