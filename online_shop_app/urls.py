from django.urls import path
from online_shop_app.apps import OnlineShopAppConfig
from online_shop_app.views import ProductListView, contacts, ProductDetailView, ProductCreateView

app_name = OnlineShopAppConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('online_shop_app/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('online_shop_app/create/', ProductCreateView.as_view(), name='product_create'),
]
