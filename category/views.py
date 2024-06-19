from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import category
from store.models import products


# Create your views here.
def store(request,slug=None):
    categories=None
    product=None
    if slug!=None:
        categories=get_object_or_404(category,slug=slug)
        product=products.objects.all().filter(category_name=categories)
    else:

        categories=category.objects.all()
        product=products.objects.all()

    context={ 
        'product':product,
        'category':categories,

        }
    print(context)
    return render(request,'store.html',context=context)