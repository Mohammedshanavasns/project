# from django.db import models
# import uuid
#
#
# class Product(models.Model):
#     PRODUCT_TYPES = [
#         ('TV', 'TV'),
#         ('Speaker', 'Speaker'),
#         ('Refrigerator', 'Refrigerator'),
#         ('AC', 'AC'),
#     ]
#
#     # Common fields for all products
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#     product_type = models.CharField(max_length=50, choices=PRODUCT_TYPES)
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     brand = models.CharField(max_length=255)
#     category = models.CharField(max_length=255)
#     stock_quantity = models.PositiveIntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     # TV-specific fields
#     screen_size = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # in inches
#     resolution = models.CharField(max_length=50, null=True, blank=True)  # e.g., '4K', '1080p'
#     panel_type = models.CharField(max_length=50, null=True, blank=True)  # e.g., 'LED', 'OLED'
#     smart_tv = models.BooleanField(null=True, blank=True)
#     hdmi_ports = models.PositiveIntegerField(null=True, blank=True)
#     usb_ports = models.PositiveIntegerField(null=True, blank=True)
#     refresh_rate = models.PositiveIntegerField(null=True, blank=True, help_text='In Hz')
#     operating_system = models.CharField(max_length=50, null=True, blank=True)
#     tv_energy_rating = models.CharField(max_length=10, null=True, blank=True)  # separate from AC energy rating
#
#     # Speaker-specific fields
#     speaker_type = models.CharField(
#         max_length=50,
#         choices=[("Bluetooth", "Bluetooth"), ("Wired", "Wired")],
#         null=True,
#         blank=True
#     )
#     connectivity = models.CharField(
#         max_length=50,
#         choices=[("Bluetooth", "Bluetooth"), ("AUX", "AUX"), ("USB", "USB"), ("Wi-Fi", "Wi-Fi")],
#         null=True,
#         blank=True
#     )
#     power_source = models.CharField(
#         max_length=50,
#         choices=[("Battery", "Battery"), ("Wired", "Wired")],
#         null=True,
#         blank=True
#     )
#     frequency_range = models.CharField(max_length=50, null=True, blank=True)  # e.g., '20Hz - 20kHz'
#     weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # in kg
#     speaker_features = models.TextField(null=True, blank=True)  # additional features
#     speaker_release_date = models.DateField(null=True, blank=True)
#     speaker_image = models.ImageField(upload_to="speaker_images/", null=True, blank=True)
#
#     # Refrigerator-specific fields
#     capacity = models.DecimalField(
#         max_digits=5,
#         decimal_places=2,
#         null=True,
#         blank=True,
#         help_text="Capacity in cubic feet"
#     )
#     door_style = models.CharField(
#         max_length=50,
#         null=True,
#         blank=True,
#         help_text="e.g., French Door, Side-by-Side"
#     )
#     refrigerator_energy_rating = models.CharField(max_length=5, null=True, blank=True)
#     has_water_dispenser = models.BooleanField(null=True, blank=True)
#     has_ice_maker = models.BooleanField(null=True, blank=True)
#     refrigerator_image = models.ImageField(upload_to="refrigerator_images/", null=True, blank=True)
#
#     # AC-specific fields
#     ac_type = models.CharField(
#         max_length=50,
#         choices=[("Split", "Split"), ("Window", "Window"), ("Portable", "Portable")],
#         null=True,
#         blank=True
#     )
#     ac_capacity = models.DecimalField(
#         max_digits=4,
#         decimal_places=2,
#         null=True,
#         blank=True,
#         help_text="Capacity in Tons"
#     )
#     ac_energy_rating = models.CharField(
#         max_length=10,
#         choices=[("3 Star", "3 Star"), ("5 Star", "5 Star")],
#         null=True,
#         blank=True
#     )
#     ac_features = models.TextField(null=True, blank=True)
#     noise_level = models.DecimalField(
#         max_digits=4,
#         decimal_places=2,
#         null=True,
#         blank=True,
#         help_text="Noise in dB"
#     )
#     ac_release_date = models.DateField(null=True, blank=True)
#     ac_image = models.ImageField(upload_to="ac_images/", null=True, blank=True)
#
#     def _str(self):  # Note: use __str_ (with double underscores)
#         return f"{self.name} - {self.product_type}"
#
#     class Meta:
#         db_table = "products"
#
#
# class ProductImage(models.Model):
#     product = models.ForeignKey(
#         Product,
#         on_delete=models.CASCADE,
#         related_name="images"
#     )
#     image = models.ImageField(upload_to="product_images/")
#     caption = models.CharField(max_length=255, blank=True)
#
#     def _str_(self):
#         return f"Image for {self.product.name}"



from django.db import models
import uuid

from brand.models import Brand
from category.models import Category


class Product_type(models.Model):
    screen_size = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    resolution = models.CharField(max_length=50, null=True, blank=True)
    panel_type = models.CharField(max_length=50, null=True, blank=True)
    hdmi_ports = models.PositiveIntegerField(null=True, blank=True)
    usb_ports = models.PositiveIntegerField(null=True, blank=True)
    refresh_rate = models.PositiveIntegerField(null=True, blank=True)
    operating_system = models.CharField(max_length=50, null=True, blank=True)
    energy_rating = models.CharField(max_length=10, null=True, blank=True)
    speaker_type = models.CharField(max_length=50, choices=[("Bluetooth", "Bluetooth"), ("Wired", "Wired")], null=True, blank=True)
    connectivity = models.CharField(max_length=50, choices=[("Bluetooth", "Bluetooth"), ("AUX", "AUX"), ("USB", "USB"), ("Wi-Fi", "Wi-Fi")], null=True, blank=True)
    power_source = models.CharField(max_length=50, choices=[("Battery", "Battery"), ("Wired", "Wired")], null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    capacity = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text="Capacity in cubic feet")

    def __str__(self):
        return f"{self.operating_system} {self.resolution} {self.refresh_rate}"

    class Meta:
        db_table = "product_types"


class Product(models.Model):
    PRODUCT_TYPES = [
        ('TV', 'TV'),
        ('Speaker', 'Speaker'),
        ('Refrigerator', 'Refrigerator'),
        ('AC', 'AC'),
        ('MOBILE', 'MOBILE')
        # New product types can be added without modifying this schema.
    ]

    # Common fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    product_type = models.ForeignKey(Product_type, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    release_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Flexible field for product-specific attributes
    dynamic_properties = models.JSONField(
        null=True,
        blank=True,
        help_text=("Store custom fields for each product type. "
                   "For example, a TV may have keys like 'screen_size', 'resolution', etc., "
                   "while a Speaker might have 'speaker_type' or 'connectivity'.")
    )

    def _str_(self):
        return f"{self.name} - {self.product_type}"

    class Meta:
        db_table = "products"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL, null=True,
        related_name="images"
    )
    image = models.ImageField(upload_to="product_images/")
    caption = models.CharField(max_length=255, blank=True)

    def _str_(self):
        return f"Image for {self.product.name}"
