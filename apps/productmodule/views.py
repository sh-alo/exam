from django.shortcuts import render,redirect
from apps.productmodule.models import Category,Product
from apps.productmodule.forms import *
# Create your views here.

def index(request):
    return render(request,'index.html')


def edit(request,id):
    product_instance = Product.objects.get(id=id)
    form = ProductForm(instance=product_instance)
    if request.POST:
        if form.is_valid():
            form.save(instance=product_instance)
            return render(list)
    return render(request,'add.html',{'form':form})
        
    
    
def list(request):
    obs = Product.objects.all()
    return render(request,'list.html',{'obs':obs})



def show(request,id):
    ob = Product.objects.get(id=id)
    return render(request,'view.html',{'ob':ob})


def delete(request,id):
    ob = Product.objects.get(id=id)
    ob.delete()
    return redirect(list)


def add(request):
    form = ProductForm()
    if request.method=='POST':
        form =  ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(list)
        
    return render(request,'add.html',{'form':form})


def search(request):
    if request.method=='POST':
        name = request.POST.get('search')  
        if (Product.objects.filter(name=name).exists()):
             ob = Product.objects.filter(name=name)
             return render(request,'view.html',{'ob':ob})
    return render(request,'search.html')