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
]

urlpatterns += [
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>/', views.BloggerDetailView.as_view(), name="blogger-detail"),
    path('blogger/<int:pk>/update/', views.BloggerUpdateView.as_view(), name='blogger-update'),
    path('blogger/create/', views.BloggerCreateView.as_view(), name='blogger-create'),
    path('blogger/<int:pk>/delete/', views.BloggerDeleteView.as_view(), name='blogger-delete'),
]
