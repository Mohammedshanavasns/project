from django.contrib import admin
from .models import Order, OrderItem, CartItem, Temporder, TempOrderItem
from .models import Cart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")
    search_fields = ("user",)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product_name", "quantity", "unit_price", "subtotal")
    search_fields = ("product_name",)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "user", "status", "total_amount", "created_at")
    search_fields = ("order_number", "user__username")
    list_filter = ("status",)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product_name", "quantity", "unit_price", "subtotal")

@admin.register(Temporder)
class TemporderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "user", "status", "total_amount", "created_at")
    search_fields = ("order_number", "user__username")
    list_filter = ("status",)


# @admin.register(TempOrderItem)
class TempOrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product_name", "quantity", "unit_price", "subtotal")


admin.site.register(TempOrderItem, TempOrderItemAdmin)
