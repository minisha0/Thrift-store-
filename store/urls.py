
from django.contrib import admin
from django.urls import path
from .views import *
from . import views

from rest_framework.routers import SimpleRouter

routers=SimpleRouter()
routers.register('categories',CategoryViewset,basename='category')
routers.register('products',ProductViewset,basename='product')
routers.register('customers',CustomerViewset,basename='customer')
routers.register('carts',CartViewset,basename='cart')
routers.register('cart-items',CartItemViewset,basename='cart-items')
routers.register('orders',OrderViewset,basename='order')
routers.register('reviews',ReviewViewset,basename='review')

urlpatterns = [
    
    
    path('',views.homepage,name='home'),
   
    path('product/',views.productpage),
    
    path('product/<id>',views.productdetailpage),
    
    path('cart/',views.cartpage),
    path('account/register/',views.register),
    
    
path('account/',views.accountpage, name='account_page'),
    
    path('add/', views.addproduct),
]
