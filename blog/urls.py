from django.urls import path

from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path(path('', BlogArticleListView.as_view(), name='blog_list'),
         path('online_shop_app/<int:pk>', BlogArticleDetailView.as_view(), name='blog_detail'),
         path('online_shop_app/create/', BlogArticleCreateView.as_view(), name='blog_create'),
         path('online_shop_app/<int:pk>/update/', BlogArticleUpdateView.as_view(), name='blog_update'),
         path('online_shop_app/<int:pk>/delete/', BlogArticleDeleteView.as_view(), name='blog_delete'), ),

]
