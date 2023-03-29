from django.contrib import admin
from django.urls import path, include
from shop.views import pageNotFound

urlpatterns = [
    # admin panel
    path('admin/', admin.site.urls),
    # my app shop
    path('', include('shop.urls')),

]

handler404 = pageNotFound
