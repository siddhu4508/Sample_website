# x from .forms import OrderForm
from .models import Order, Product, Delivery
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login 


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login the user after registration
            auth_login(request, user)
            return redirect('app/dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def dashboard(request):
    user = request.user
    orders = Order.objects.all()
    #orders = Order.objects.filter(customer=request.user)
    return render(request, 'app/dashboard.html', {'orders': orders})


@login_required
def order_history(request):
    # Retrieve order history for the current user
    orders = Order.objects.all()
    #orders = Order.objects.filter(customer=request.user)
    return render(request, 'app/order_history.html', {'orders': orders})


def product_catalog(request):
    products = Product.objects.all()
    return render(request, 'app/product_catalog.html', {'products': products})

def product_details(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {product:product})


# views.py


@login_required
def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Process order
            form.save()
            return redirect('order_confirmation')
    else:
        form = OrderForm()
    return render(request, 'app/place_order.html', {'form': form})


@login_required
def delivery_status(request):
    deliveries = Delivery.objects.all()
    #deliveries = Delivery.objects.filter(customer=request.user)
    return render(request, 'app/delivery_status.html', {'deliveries': deliveries})


@login_required
def manage_subscription(request):
    subscription = Subscription.objects.get(customer=request.user)
    # Logic for managing subscription
    return render(request, 'app/manage_subscription.html', {'subscription': subscription})
