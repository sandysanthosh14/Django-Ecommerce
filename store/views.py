from django.shortcuts import render
from .models import products
from category.models import category
from django.shortcuts import get_object_or_404
from category.models import category
from .models import products

# Create your views here.
def product(request):
    categories=category.objects.all()
    product=products.objects.all()
    context={ 
        'product':product,
        'category':categories,

    }
    print(context)
    return render(request,'home.html',context=context)



# Create your views here.
'''def store(request,category_slug=None):
    categories=None
    product=None
    if category_slug!=None:
        categories=get_object_or_404(category,slug=category_slug)
        product=products.objects.all().filter(category_name=categories)
    else:

        categories=category.objects.all()
        product=products.objects.all()

    context={ 
        'product':product,
        'category':categories,

        }
    print(context)
    return render(request,'store.html',context=context)'''

def product_details(request,category_slug,product_slug):
    product=get_object_or_404(products,category_name__slug=category_slug,slug=product_slug)
    print(product)
    return render(request,'product_details.html',context={'product':product})

