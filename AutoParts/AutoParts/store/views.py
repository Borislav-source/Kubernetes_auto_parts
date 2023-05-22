import datetime
import json
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from AutoParts.accounts.models import Profile
from AutoParts.parts.models import Product
from AutoParts.store.models import Order, OrderItem, ShippingAddress


def cart(request):
    if request.user.is_authenticated:
        customer = Profile.objects.get(user=request.user)

        try:
            order = Order.objects.get(customer=customer, complete=False)
            items = order.orderitem_set.all()
        except:
            items = None
            order = None

        context = {
            'items': items,
            'order': order,
            'car': customer.car,
        }
        return render(request, 'store/cart.html', context)
    messages.success(request, 'You need to be sign in')
    return render(request, 'pages/index.html')


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = Profile.objects.get(user=request.user)
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added successfully', safe=False)


def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    customer = Profile.objects.get(user=request.user)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_total_for_cart:
        order.complete = True
    order.save()

    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        country=data['shipping']['country'],
        zipcode=data['shipping']['zipcode'],
    )
    return JsonResponse('Payment completed!', safe=False)


def checkout(request):
    customer = Profile.objects.get(user=request.user)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    context = {
        'items': order.orderitem_set.all(),
        'order': order,
    }
    return render(request, 'store/checkout.html', context)
