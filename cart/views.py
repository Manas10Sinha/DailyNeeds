from django.shortcuts import render, redirect
from cart.models.product import Product
from cart.models.category import Category
from cart.models.locality import Locality
from cart.models.order import Order
from django.views import View
from .form import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Avg, Sum, Max, Min, Count
from datetime import date
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, "index.html")

def ul(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "login successfully!!")
                    request.session['user_id'] = user.id
                    request.session['email'] = user.email
                    request.session['first_name'] = user.first_name
                    request.session['last_name'] = user.last_name

                    print('you 2 are=', request.session.get('email'))
                    print('you 2 are=', request.session.get('user_id'))
                    print('you 2 are=', request.session.get('last_name'))
                    return HttpResponseRedirect('/Shop/')
            else:
                messages.error(request, "Invalid Login")
                return redirect('/ul')
        else:
            fm = AuthenticationForm()
            return render(request, 'ul.html', {'form': fm})
    else:
        return HttpResponseRedirect('/')

class Shop(View):
    def post(self,request):
        print("test2")
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            print(quantity)
            if quantity:
                if remove:
                   if quantity <= 1:
                        cart.pop(product)
                   else:
                        cart[product] = quantity - 1
                else:
                        cart[product] = quantity + 1
            else:
                 cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print("cart", request.session['cart'])
        return redirect("/query/")

    def get(self,request):
            print("test3")
            cart = request.session.get('cart')
            print(cart)
            if not cart:
                request.session['cart'] = {}

            product = None
            categories = Category.get_all_categories()
            #print(request.GET)
            categoryID = request.GET.get('category')

            localities = Locality.get_all_localities()
            localityID = request.GET.get('locality')
            print(localityID)
            if(localityID):
                products = Product.get_all_products_by_localityid(localityID)

                data = {}
                data['products'] = products
                data['localities'] = localities
                print('You are :', request.session.get('email'))
                return render(request, 'shop.html', data)

            print(categoryID)
            if (categoryID):
                products = Product.get_all_products_by_catgegoryid(categoryID)

                data = {}
                data['products'] = products
                data['categories'] = categories

                print('You are :', request.session.get('email'))
                return render(request, 'shop.html', data)

            else:
                sort = Product.objects.order_by("-price")
                context = {'sort': sort}
                print('You are :', request.session.get('email'))
                return render(request, 'shop.html', context)




def query(request):
        if request.method == 'POST':
            locality = request.session.get('last_name')
            category = request.POST["category"]
            print(locality)
            print(category)


            localities = Locality.get_all_localities()
            products = Product.get_all_products_by_locality(locality,category)
            minimum = products.aggregate(Min('price'))
            count = products.aggregate(Count('price'))

            data = {}
            data['products'] = products
            data['localities'] = localities
            data['minimum'] = minimum
            data['count'] = count

            print('You are :', request.session.get('email'))
            return render(request,'shop.html', data)
        else:
            return render(request, 'query.html')


class Cart(View):
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        print(ids)
        products = Product.get_products_by_ids(ids)
        print(products)
        return render(request, 'cart.html', {'products': products})




class Bill(View):
    def get(self, request):
        Date = date.today()
        customer = request.session.get('email')
        orders = Order.get_orders_by_date(Date,customer)
        print(orders)
        return render(request, 'Bill.html', {'orders': orders})

class Orderview(View):
    def post(self,request):
        date = request.POST["date"]
        orders = Order.get_orders_by_date2(date)
        print(orders)
        return render(request, 'order.html', {'orders': orders})
    def get(self,request):
        return render(request, 'order.html')

def Challan(request):
    if request.method == 'POST':
        Shop = request.POST["Shop"]
        date = request.POST["date"]

        print(Shop)
        orders = Order.get_orders_by_shop(Shop,date)
        print(orders)
        return render(request, 'challan.html', {'orders': orders})
    else:
        return render(request, 'challan.html')

class Checkout(View):
        def post(self, request):
            if  request.user.is_authenticated:
                address = request.POST.get('address')
                phone = request.POST.get('phone')
                cart = request.session.get('cart')
                products = Product.get_products_by_ids(list(cart.keys()))

                for product in products:
                    order = Order(customer = request.session.get('email'),
                              product = product ,
                              price = product.price ,
                              Shop = product.Shop,
                              mobile = product.mobile,
                              address = address ,
                              phone = phone ,
                              quantity = cart.get(str(product.id)))
                    order.save()

                request.session['cart'] = {}

                return redirect('cart')
            else:
                messages.error(request, "Please ! Login")
                return redirect('/ul/')


def sign_up(request):
      if request.method == 'POST':
            fm = SignUpForm(request.POST)
            #fm = UserCreationForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Account  has been created successfully!!")
      else:
                fm = SignUpForm()
                #fm = UserCreationForm()
      return render(request, 'sign_up.html', {'form': fm})



def user_logout(request):
    logout(request)
    messages.success(request, "You are logged out")
    return redirect('/')

def user_profile(request):

        categoryID = request.POST.get('category')
        print(categoryID)
        return render(request, 'profile.html', {'name': request.user})


def about(request):

    return render(request, 'about.html')

def terms(request):

    return render(request, 'terms.html')

def refund(request):

    return render(request, 'refund.html')

def shops(request):

    return render(request, 'shops.html')

def shop1(request):
    name="Rajesh"
    products = Product.get_all_products_by_shop(name)
    data = {}
    data['products'] = products
    return render(request, 'shop1.html',data)

def shop2(request):
    name="Chotu"
    products = Product.get_all_products_by_shop(name)
    data = {}
    data['products'] = products
    return render(request, 'shop2.html',data)


