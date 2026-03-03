from django.contrib import admin
from order.models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

# Register your models here.
# admin.site.register(Cart)
admin.site.register(CartItem)