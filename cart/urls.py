from django.urls import path
from .views import  Shop, Cart, Checkout, Orderview,  Bill
from cart import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
      path('', views.index, name='index'),
      path('Shop/', Shop.as_view(), name='Shop'),
      path('Cart/', Cart.as_view(), name='cart'),
      path('Challan/',views.Challan, name='challan'),
      path('Bill/',Bill.as_view(), name='bill'),
      path('Bill2/',views.Bill2, name='bill2'),
      path('sign_up/',  views.sign_up , name='sign_up'),
      path('sign_up/sign_up/', views.sign_up, name='sign_up'),
      path('ul/', views.ul, name='ul'),
      #path('ul/ul/', views.ul, name='ul'),
      path('user_profile/', views.user_profile, name='profile'),
      path('user_logout/', views.user_logout, name='user_logout'),
      path('about/', views.about, name='about'),
      path('terms/', views.terms, name='terms'),
      path('refund/', views.refund, name='refund'),
      path('shops/', views.shops, name='shops'),
      path('shop1/', views.shop1, name='shop1'),
      path('shop2/', views.shop2, name='shop2'),
      path('query/', views.query, name='query'),
      path('harry/', views.harry, name='harry'),

      path('check-out', Checkout.as_view() , name='checkout'),
      path('Orderview/', Orderview.as_view() , name='order'),
      path('proinfo/', views.product_detail),
      path('proinfo/', views.product_detail),
      path('gettoken/', obtain_auth_token)




]