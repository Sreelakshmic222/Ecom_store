from accounts .views import home,about,contact,cart

from django.urls import path
from . import views
from .views import Index

app_name = "accounts"


urlpatterns = [
        path("register", views.register_request, name="register"),
        path("login", views.login_request, name="login"),
        path('',Index.as_view(),name='index'),
        path('home/',home,name="home"),
        path('about/',about,name="about"),
        path('contact/',contact,name="contact"),
        path("cart/",cart,name="cart")


]