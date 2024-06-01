from django.urls import path
from online_shop_app.apps import OnlineShopAppConfig
from online_shop_app.views import home, contacts, products_detail

app_name = OnlineShopAppConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>', products_detail, name='products_detail')
]
