from django.db import models
from .category import Category
from .locality import Locality
from .sub_locality import Sub_locality


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    oprice = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, default=1)
    sub_locality = models.ForeignKey(Sub_locality, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200)
    Shop = models.CharField(max_length=200,default='')
    mobile = models.IntegerField(default=0)
    image = models.ImageField(upload_to='upload/products/')

    @staticmethod
    def get_products_by_ids(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_all_products():
                products = Product.objects.all()
                return (products)

    @staticmethod
    def get_all_products_by_catgegoryid(category_id):
            if category_id:
                return Product.objects.filter(category = category_id)
            else:
                return Product.get_all_products()

    @staticmethod
    def get_all_products_by_localityid(locality_id):
        if locality_id:
            return Product.objects.filter(locality=locality_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_all_products_by_locality(loc, cat):
            return Product.objects.filter(locality=loc, category=cat)

    @staticmethod
    def get_all_products_by_shop(name):
        return Product.objects.filter(Shop=name)

    def __str__(self):
        return self.name