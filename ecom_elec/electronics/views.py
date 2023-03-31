from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse_lazy
from .models import Elec, Order,Cart,favorite
from django.views.generic import ListView,DetailView
import json
from django.http import JsonResponse
# Create your views here.

class ElecListView(ListView):
    model = Elec
    template_name = 'list.html'

class ElecDetailView(DetailView):
    model= Elec
    template_name='detail.html'

class ElecCheckoutView(DetailView):
    model= Elec
    template_name = 'checkout.html'

def PaymentComplete(request):
    body = json.loads(request.body)
    print('BODY:',body)
    product=Elec.objects.get(id=body['productId'])
    Order.objects.create(product=product)
    return JsonResponse('payment completed',safe=False)

class SearchResultsView(ListView):
    model=Elec
    template_name= 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Elec.objects.filter(Q(name=query)|Q(Company=query))

def add_to_cart(request, pk):
    Product = get_object_or_404(Elec, pk=pk)
    cart_item,created = Cart.objects.get_or_create(
        user=request.user,
        product= Product,
        price=Product.price,
        image_url = Product.image_url,
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, pk=cart_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})



def add_fav(request, pk):
    Product = get_object_or_404(Elec,pk=pk)
    favorite_item,created = favorite.objects.get_or_create(
        user=request.user,
        product= Product,
        image_url = Product.image_url,
        price=Product.price,
        stock_availability=Product.stock_availability

    )
    if not created:
        favorite_item.quantity += 1
        favorite_item.save()
    return redirect('fav')


def remove_from_fav(request, fav_id):
    favorite_item = get_object_or_404(favorite, pk=fav_id, user=request.user)
    if favorite_item.quantity == 0:
        favorite_item.quantity -= 1
        favorite_item.save()
    else:
        favorite_item.delete()
    return redirect('fav')

def fav(request):
    favorite_items = favorite.objects.filter(user=request.user)
    return render(request, 'fav.html', {'favorite_items': favorite_items})