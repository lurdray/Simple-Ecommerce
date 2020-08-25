from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import date
from django.utils import timezone
from .models import Order, Product
# Create your views here.

def IndexView(request):

	products = Product.objects.order_by("-pub_date")
	
	context = {"products": products}
	return render(request, "mainapp/index.html", context)
	
def AboutView(request):
	context = {}
	return render(request, "mainapp/about.html", context)
	

def DashboardView(request):
	if request.method == "POST":
		name = request.POST.get("name")
		pub_date = timezone.now()
		image = request.FILES["image"]
		descrp = request.POST.get("descrp")
		
		product = Product.objects.create(name=name, image=image, descrp=descrp, pub_date=pub_date)
		product.save()
		return HttpResponseRedirect(reverse("mainapp:dashboard"))
		
	else:
		orders = Order.objects.order_by('-pub_date')
		products = Product.objects.order_by("-pub_date")
	
		context = {"orders": orders, "products": products}
		return render(request, "mainapp/dashboard.html", context)
	
def OrderDetailView(request, order_id):
	order = get_object_or_404(Order, pk=order_id)
	product = get_object_or_404(Product, pk=order.product_id)
	context = {"order": order, "product": product}
	return render(request, "mainapp/order_detail.html", context)
	
def ProductDetailView(request, product_id):
	
	if request.method == "POST":
		quantity = request.POST.get("quantity")
		pub_date = timezone.now()
		comment = request.POST.get("comment")
		phone_owner = request.POST.get("phone_owner")
		email_owner = request.POST.get("email_owner")
		name_owner = request.POST.get("name_owner")
		
		
		order = Order.objects.create(product_id=product_id, quantity=quantity, name_owner=name_owner, phone_owner=phone_owner, email_owner=email_owner, comment=comment, pub_date=pub_date)
		
		order.save()
		return HttpResponseRedirect(reverse("mainapp:index"))
	
	else:
		product = get_object_or_404(Product, pk=product_id)
		context = {"product": product}
		return render(request, "mainapp/product_detail.html", context)
	

def ProductView(request):
	context = {}
	return render(request, "mainapp/product.html", context)
	
def RemoveProductView(request, d_product_id):
	Product.objects.filter(pk=d_product_id).delete()
	Order.objects.filter(product_id=d_product_id).delete()
	return HttpResponseRedirect(reverse("mainapp:dashboard"))
	#if request.method == "POST":

	#else:
	#	return render(request, "mainapp/delete_product.html")
	#return HttpResponse("asdfg")
	#if request.method == "GET":
	#product = get_object_or_404(Product, pk=product_id)
	
	
def RemoveOrderView(request, d_order_id):
	Order.objects.filter(pk=d_order_id).delete()
	return HttpResponseRedirect(reverse("mainapp:dashboard"))
	
