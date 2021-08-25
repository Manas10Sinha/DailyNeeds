from django.db import models
from .product import Product
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    customer = models.CharField(max_length=50 , default='')
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50 , default='' )
    phone = models.CharField(max_length=50 , default='')
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    Shop = models.CharField(max_length=200, default='')
    mobile = models.IntegerField(default=0)


    @staticmethod
    def get_orders_by_customer(customer):
         return Order\
             .objects\
             .filter( customer = customer )\
            .order_by('-date')

    def get_orders_by_date2(date):
         return Order\
             .objects\
             .filter( date = date )\
            .order_by('-date')

    @staticmethod
    def get_orders_by_shop(Shop,date):
         return Order\
             .objects\
             .filter( Shop = Shop, date = date)\
            .order_by('-date')

    @staticmethod
    def get_orders_by_date(date,customer):
         return Order\
             .objects\
             .filter( date = date, customer = customer )\
            .order_by('-date')