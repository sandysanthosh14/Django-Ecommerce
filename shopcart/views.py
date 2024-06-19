from django.shortcuts import render
from category.models import category
from store.models import products


# Create your views here.
def home(request):
    categories=category.objects.all()
    product=products.objects.all()
    context={ 
        'product':product,
        'category':categories,

    }
    print(context)
    return render(request,'home.html',context=context)

def store(request):
    return render(request,'home.html')
