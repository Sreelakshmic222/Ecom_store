from django.urls import path
from .views import ElecListView, ElecDetailView, ElecCheckoutView, PaymentComplete,SearchResultsView
from . import views
urlpatterns=[
    path('elec_list/',ElecListView.as_view(),name='list'),
    path('details/<int:pk>/',ElecDetailView.as_view(),name='detail-view'),
    path('checkout/<int:pk>/',ElecCheckoutView.as_view(),name='checkout'),
    path('complete',PaymentComplete,name='complete'),
    path('search',SearchResultsView.as_view(),name='search'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('fav/add/<int:pk>/', views.add_fav, name='add_to_fav'),
    path('fav/remove/<int:fav_id>/', views.remove_from_fav, name='remove_from_fav'),
    path('fav/', views.fav, name='fav'),

]