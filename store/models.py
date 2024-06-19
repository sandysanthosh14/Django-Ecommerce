from django.db import models
from category.models import category
from django.urls import reverse

# Create your models here.
class products(models.Model):
    product_name=models.CharField(null=False,blank=False,max_length=100)
    price=models.IntegerField(null=False,blank=False)
    category_name=models.ForeignKey(category,null=False,blank=False,on_delete=models.CASCADE)
    is_available=models.BooleanField(default=True)
    status_choice = (
        ('small', 'S'),
        ('medium', 'M'),
        ('large', 'L'),
    )
    size=models.CharField(max_length=30,choices=status_choice)
    quentity=models.IntegerField()
    bio=models.TextField(max_length=300,blank=True)
    image=models.ImageField(upload_to='photos/protects',null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.product_name
    
    def get_url(self):
        return reverse('product_details',kwargs={'category_slug':self.category_name,'product_slug':self.slug})