
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
    
    
    path('',views.homepage),
   
    path('product/',views.productpage),
    
    path('productdetail/',views.productdetailpage),
    
    path('cart/',views.cartpage),
    
    
    path('account/',views.accountpage),
    
    path('add/', views.addproduct),
]
