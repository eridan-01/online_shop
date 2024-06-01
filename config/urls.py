from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('online_shop_app.urls', namespace='online_shop_app'))
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
