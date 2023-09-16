from django.contrib import admin
from .models import Kuntic, Material, Size, Color, Order

admin.site.register(Kuntic)
admin.site.register(Order)
admin.site.register(Material)
admin.site.register(Size)
admin.site.register(Color)