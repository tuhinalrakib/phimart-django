from django.contrib import admin
from order.models import Cart, CartItem, Order, OrderItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status']

# Register your models here.
# admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderItem)