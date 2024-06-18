from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogArticleCreateView, BlogArticleListView, BlogArticleDetailView, BlogArticleUpdateView, \
    BlogArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogArticleListView.as_view(), name='list'),
    path('view/<int:pk>', BlogArticleDetailView.as_view(), name='view'),
    path('create/', BlogArticleCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', BlogArticleUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogArticleDeleteView.as_view(), name='delete')
]
