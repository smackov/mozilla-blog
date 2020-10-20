from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name="blog-detail"),
    path('blog/<int:pk>/update/', views.BlogUpdateView.as_view(), name='blog-update'),
    path('blog/create/', views.BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog-delete'),
    path('blog/<int:pk>/create_comment/', views.BlogCommentCreateView.as_view(), name='blog-comment-create'),
]

urlpatterns += [
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>/', views.BloggerDetailView.as_view(), name="blogger-detail"),
]
