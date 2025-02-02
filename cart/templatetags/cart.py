from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
              print('a',product.name)
              return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product , cart):
    keys = cart.keys()
    print(keys)
    for id in keys:
        if int(id) == product.id:
            print('b',product.name)
            return cart.get(id)
    return 0

@register.filter(name='price_total')
def price_total(product, cart ):
    return product.price * cart_quantity(product,cart)

@register.filter(name='total_cart_price')
def total_cart_price(products, cart ):
    sum = 0
    for p in products:
        sum += price_total(p , cart)
    return sum

@register.filter(name='total_cart_quantity')
def total_cart_quantity(products, cart ):
    sum = 0
    for p in products:
        sum += cart_quantity(p , cart)
    return sum









@register.filter(name='price2_total')
def price2_total(order, cart ):
    return order.product.price * order.quantity

@register.filter(name='total_cart_price2')
def total_cart_price2(orders, cart ):
    sum = 0
    for p in orders:
        sum += price2_total(p , cart)
    if sum < 500 :
        return sum+50
    else:
        return sum


