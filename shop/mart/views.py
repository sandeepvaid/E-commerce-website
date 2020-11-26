from django.shortcuts import render
from .models import products,Order
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    product = products.objects.all()

    #Search code
    item_name=request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        product = product.filter(title__icontains=item_name)

    #paginator code
    paginator=Paginator(product,4)   
    page = request.GET.get('page')
    product = paginator.get_page(page)
    return render(request,"mart/index.html",{'product':product})

def detail(request,id):
    product_object = products.objects.get(id=id)

    return render(request,'mart/detail.html',{"product_object":product_object})

def checkout(request):
    if request.method=="POST":
        item = request.POST.get('item',"")
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zipcode = request.POST.get('zipcode', '')
        total = request.POST.get('total','')

        order = Order(item=item ,name=name,email = email,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save()
    return render(request,'mart/checkout.html')    
