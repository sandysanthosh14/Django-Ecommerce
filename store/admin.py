from django.contrib import admin
from.models import products

# Register your models here.
class productadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':['product_name']}
    list_display=['product_name','slug','price','quentity','category_name','created_date']
    
    
admin.site.register(products,productadmin)
