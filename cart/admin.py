from django.contrib import admin

# Register your models here.
from .models.product import Product
from .models.category import Category
from .models.locality import Locality
from .models.sub_locality import Sub_locality
from .models.order import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
        list_display = ['name']


class AdminLocality(admin.ModelAdmin):
    list_display = ['name']

class AdminSub_locality(admin.ModelAdmin):
    list_display = ['name']

class AdminOrder(admin.ModelAdmin):
    list_display = ['product', 'customer', 'quantity', 'price' , 'address' , 'phone' , 'date']

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Locality, AdminLocality)
admin.site.register(Sub_locality, AdminSub_locality)
admin.site.register(Order, AdminOrder)