from django.urls import path
from online_shop_app.apps import OnlineShopAppConfig
from online_shop_app.views import home, contacts

app_name = OnlineShopAppConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]
