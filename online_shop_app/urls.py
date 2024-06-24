from django.urls import path
from online_shop_app.apps import OnlineShopAppConfig
from online_shop_app.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ContactView, VersionCreateView, VersionUpdateView

app_name = OnlineShopAppConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('online_shop_app/contacts/', ContactView.as_view(), name="contacts"),
    path('online_shop_app/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('online_shop_app/create/', ProductCreateView.as_view(), name='product_create'),
    path('online_shop_app/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('online_shop_app/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:product_id>/add_version/', VersionCreateView.as_view(), name='version_add'),
    path('versions/<int:pk>/update/', VersionUpdateView.as_view(), name='version_update'),
]
