from django.shortcuts import render,get_object_or_404,redirect

#Messages
from django.contrib import messages
#Authentications
from django.contrib.auth.decorators import login_required

#Model
from .models import Hotel,Bookings
from store.models import Product
# Create your views here.
@login_required
def add_to_cart(request,pk):
    item = get_object_or_404(Product,id=pk)
    order_item = Hotel.objects.get_or_create(item=item,user=request.user,purchased=False)
    order_qs = Bookings.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request,"This item quantity was updated.")
            return redirect("home")
        else:
            order.orderitems.add(order_item[0])
            messages.info(request,"This item is added to your cart.")
            return redirect("home")
    
    else:
        order = Bookings(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request,"This item is added to your cart.")
        return redirect("home")


@login_required
def cart_view(request):
    carts = Hotel.objects.filter(user=request.user,purchased=False)
    orders = Hotel.objects.filter(user=request.user,ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request,'store/cart.html',context={'carts':carts,'order':order})

    else:
        messages.warning(request,"You don't have any item in your cart!")
        return redirect("home")

@login_required
def remove_from_cart(request,pk):
    item = get_object_or_404(Product,id=pk)
    order_qs = Hotel.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Hotel.objects.filter(item=item,user=request.user,purchased=False)
            order_item = order_item[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request,"This item is remove from your cart!")
            return redirect("cart")
        else:
            messages.info(request,"This item was not in your cart.")
            return redirect("home")
    else:
        messages.info(request,"You don't have an active order")

@login_required
def increase_cart(request,pk):
    item = get_object_or_404(Product,id=pk)
    order_qs = Hotel.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Hotel.objects.filter(item=item,user=request.user,purchased=False)[0]
            if order_item.quantity >=1:
                order_item.quantity +=1
                order_item.save()
                messages.info(request,f"{item.name} quantity has been updated!!")
                return redirect("cart")
        else:
            messages.info(request,f"{item.name} is not in your cart")
            return redirect("home")
    else:
        messages.info(request,"You don't have an active order")
        return redirect("home")


@login_required
def decrease_cart(request,pk):
    item = get_object_or_404(Product,id=pk)
    order_qs = Hotel.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Hotel.objects.filter(item=item,user=request.user,purchased=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -=1
                order_item.save()
                messages.info(request,f"{item.name} quantity has been updated!! ")
                return redirect("cart")
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request,f"{item.name} item has been removed from your cart!!")
                return redirect("cart")
        else:
            messages.info(request,f"{item.name} is not in your cart")
            return redirect("home")
    else:
        messages.info(request,"You don't have an active order")
        return redirect("home")