from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('land/', views.land, name="land"),
    path('insurance/', views.insurance, name="insurance"),
    path('contact/', views.contact, name="contact"),
    path('training/', views.training, name="training"),
]