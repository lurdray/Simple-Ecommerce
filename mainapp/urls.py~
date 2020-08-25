from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    # None
    path('', views.IndexView, name='index'),
    
    path('orderdetail/<int:order_id>/', views.OrderDetailView, name='order_detail'),
    path('productdetail/<int:product_id>/', views.ProductDetailView, name='product_detail'),
    
    path('removeproduct/<int:d_product_id>/', views.RemoveProductView, name='remove_product'),
    path('removeorder/<int:d_order_id>/', views.RemoveOrderView, name='remove_order'),
    
    path('dashboard/', views.DashboardView, name='dashboard'),
    path('about/', views.AboutView, name='about'),
    path('product/', views.ProductView, name='product'),
]
