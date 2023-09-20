from django.contrib import admin
from .models import TableModel, Booking, CategoryTableModel, ProductsModel, CategoryProductsModel

# Register your models here.
admin.site.register(TableModel)
admin.site.register(Booking)
admin.site.register(CategoryTableModel)
admin.site.register(ProductsModel)
admin.site.register(CategoryProductsModel)