from django.contrib import admin
from django.urls import path

from Shop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kuntic/<int:id_kuntic>/', product_page),
    path('catalog/', katalog_view),
    path('orders/', orders_view),
    path('create_kuntic/', create_view),
]
