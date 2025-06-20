# from django.urls import path
# from .views import vendor_dashboard, add_product
#
# urlpatterns = [
#     path('dashboard/', vendor_dashboard, name='vendor_dashboard'),
#     path('add-product/', add_product, name='add_product'),
# ]

from django.urls import path
from .views import vendor_dashboard, add_product

urlpatterns = [
    path('vendor_dashboard/', vendor_dashboard, name='vendor_dashboard'),
    path('add-product/', add_product, name='add_product'),
    # path('become/', become_vendor, name='become_vendor'),  # Optional path to allow registration
]
