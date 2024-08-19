from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('products/', views.Products,name="products"),
    path('about/', views.About,name="about"),
    path('contact/', views.Contact,name="contact"),
    path('gallery',views.Gallery,name="gallery"),
    path('user/h18a/login',views.login_view,name='login_view'),
    path('user/n3jl4/home',views.home_view,name='home_view'),
    path('user/logout',views.logout_view,name='logout_view'),
    path('user/ruh4/read',views.read,name='read'),
]
