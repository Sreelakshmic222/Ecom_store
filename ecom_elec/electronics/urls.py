from django.urls import path
from .views import ElecListView, ElecDetailView, ElecCheckoutView, PaymentComplete,SearchResultsView

urlpatterns=[
    path('elec_list/',ElecListView.as_view(),name='list'),
    path('details/<int:pk>/',ElecDetailView.as_view(),name='detail-view'),
    path('checkout/<int:pk>/',ElecCheckoutView.as_view(),name='checkout'),
    path('complete',PaymentComplete,name='complete'),
    path('search',SearchResultsView.as_view(),name='search'),

]