# from django.db import models
# import uuid
#
# class BaseCategory(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#     name = models.CharField(max_length=255, unique=True)
#     description = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True  # This ensures it's used only for inheritance
#
#     def _str_(self):
#         return self.name
#
#
#
# class ProductCategory(BaseCategory):
#     parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories')
#     is_active = models.BooleanField(default=True)
#
#     class Meta:
#         db_table = "categories_product"
#         verbose_name = "Product Category"
#         verbose_name_plural = "Product Categories"
#
#     def _str_(self):
#         return f"{self.name} (Parent: {self.parent_category.name if self.parent_category else 'None'})"

#
# from django.db import models
# import uuid
# from django.utils.text import slugify
#
# class Category(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=100, unique=True)
#     slug = models.SlugField(max_length=120, unique=True, blank=True)
#     description = models.TextField(blank=True, null=True)
#     image = models.ImageField(upload_to='category_images/', blank=True, null=True)
#     parent = models.ForeignKey(
#         'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subcategories'
#     )
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = "Category"
#         verbose_name_plural = "Categories"
#         ordering = ['name']
#         db_table = 'product_categories'
#
#     def _str_(self):
#         return self.name
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super(Category, self).save(*args, **kwargs)

from django.db import models
import uuid
from django.utils.text import slugify

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subcategories'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']
        db_table = 'product_categories'

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)