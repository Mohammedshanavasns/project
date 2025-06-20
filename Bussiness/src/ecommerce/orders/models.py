from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
# from accounts.models import Ucfd
from base.models import BaseModel

# Assuming BaseModel is in core/models.py

ORDER_STATUS_CHOICES = [
    ("PENDING", "Pending"),
    ("PROCESSING", "Processing"),
    ("COMPLETED", "Completed"),
    ("CANCELLED", "Cancelled"),
]


class Cart(BaseModel):
    user = models.CharField(max_length=122)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        verbose_name =  _('Cart')
        verbose_name_plural = _('Cart')


    def __str__(self):
        return f"Cart for {self.user}"


class CartItem(BaseModel):
    cart = models.CharField(max_length=244)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'CartItem'
        verbose_name = _('CartItem')
        verbose_name_plural = _('CartItem')


    @property
    def subtotal(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.product_name} (x{self.quantity})"


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    order_number = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default="PENDING")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.auto_id:
            last_auto_id = self._class.objects.aggregate(models.Max('auto_id'))['auto_id_max'] or 0
            self.auto_id = last_auto_id + 1
        if not self.order_number:
            self.order_number = f"ORD{self.auto_id:05d}"  # e.g., ORD00001
        super().save(*args, **kwargs)


class OrderItem(BaseModel):
    order = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'OrderItem'
        verbose_name = _('OrderItem')
        verbose_name_plural = _('OrderItem')

    @property
    def subtotal(self):
        return self.quantity * self.unit_price

    def _str_(self):
        return f"{self.product_name} (x{self.quantity})"


class Temporder(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    order_number = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default="PENDING")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.auto_id:
            last_auto_id = self._class.objects.aggregate(models.Max('auto_id'))['auto_id_max'] or 0
            self.auto_id = last_auto_id + 1
        if not self.order_number:
            self.order_number = f"ORD{self.auto_id:05d}"  # e.g., ORD00001
        super().save(*args, **kwargs)

class TempOrderItem(BaseModel):
    order = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'TempOrderItem'
        verbose_name = _('TempOrderItem')
        verbose_name_plural = _('TempOrderItem')

    @property
    def subtotal(self):
        return self.quantity * self.unit_price

    def _str_(self):
        return f"{self.product_name} (x{self.quantity})"