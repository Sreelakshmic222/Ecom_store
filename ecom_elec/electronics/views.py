from django.db.models import Q
from django.shortcuts import render
from .models import Elec, Order
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