from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'price', 'description', 'brand', 'model', 'color', 'category', 'discount']