"""
URL configuration for shopper_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('cart', views.cart, name='cart'),
    path('detail', views.detail, name='detail'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    
    path('register', views.register, name='register'),
    path('forget', views.forget, name='forget'),
    path('confirm_password', views.confirm_password, name='confirm_password'),
    path('detail1/<int:id>', views.detail1, name='detail1'),
    path('search', views.search, name='search'),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('cart_plus/<int:id>', views.cart_plus, name='cart_plus'),
    path('cart_mines/<int:id>', views.cart_mines, name='cart_mines'),
    path('cart_remove/<int:id>', views.cart_remove, name='cart_remove'),
    path('order', views.order, name='order'),
    path('order_delete/<int:id>', views.order_delete, name='order_delete'),
    path('color_filter', views.color_filter, name='color_filter'),
    path('price_filter', views.price_filter, name='price_filter'),
    path('add_whishlist/<int:id>', views.add_whishlist, name='add_whishlist'),
    path('whishlist', views.whishlist, name='whishlist'),
    path('remove_whishlist/<int:id>', views.remove_whishlist, name='remove_whishlist'),
    
    
    path('create_rating', views.create_rating, name='create_rating'),
    path('single_add_to_cart/<int:id>', views.single_add_to_cart, name='single_add_to_cart'),
    path('user_profile/<int:id>', views.user_profile, name='user_profile'),
    path('edit_profile/<int:id>/', views.edit_profile, name='edit_profile'),
    path('show_profile', views.show_profile, name='show_profile'),
    path('apply_coupon', views.apply_coupon, name='apply_coupon'),
    path('invoice', views.invoice, name='invoice'),
    path('pagi', views.pagi, name='pagi'),
    path('order_track', views.order_track, name='order_track'),
   
    
    
    
    
]

