from http.client import HTTPResponse
from unicodedata import category
from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Q
from django.contrib import messages

from category.models import Category
from .models import Product, ProductGallery,ReviewRating
from app_location.models import Location
from .forms import Reviewform
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.
def store(request,category_slug=None,location_slug=None):
    categories = None
    products = None

    if category_slug !=None:
        categories = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=categories,is_available=True)
        paginator = Paginator(products,3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()

    elif location_slug != None:
        location = get_object_or_404(Location,slug=location_slug)
        products = Product.objects.filter(location=location,is_available=True)
        paginator = Paginator(products,3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()


    else:
        products = Product.objects.all().filter(is_available=True).order_by('-id')
        paginator = Paginator(products,3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        products_count = products.count()

    context = {
        'products':paged_products,
        'product_count':products_count,
    }
    return render(request,'store/store.html',context)


def product_detail(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)

    except Exception as e:
        raise e

    reviews = ReviewRating.objects.filter(product_id =single_product.id,status=True)

    #get the product gallery
    product_gallery = ProductGallery.objects.filter(product_id=single_product.id)

    context = {
        'single_product':single_product,
        'reviews':reviews,
        'product_gallery':product_gallery
    }
    return render(request,'store/product_detail.html',context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            products_count = products.count()
    context = {
        'products':products,
        'product_count':products_count,
    }
    return render(request,'store/store.html',context)

def submit_review(request,product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id,product__id=product_id)
            form = Reviewform(request.POST,instance=reviews)
            form.save()
            messages.success(request,"Thank you! your review has been updated..")
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = Reviewform(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request,"Thank you! your review has been submitted..")
                return redirect(url)