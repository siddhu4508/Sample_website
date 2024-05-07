# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('delivery_status', views.delivery_status, name = 'delivery_status'),
    path('manage_subscription', views.manage_subscription, name = 'manage_subscription'),
    path('order_history', views.order_history, name = 'order_history'),
    path('place_order', views.place_order, name = 'place_order'),
    path('product_catalog', views.product_catalog, name = 'product_catalog'),
    path('product_details', views.product_details, name = 'product_details')
]
