from django.db import models
from django.urls import reverse

# Create your models here.
class category(models.Model):
    category_name=models.CharField(null=False,max_length=100)
    slug=models.SlugField(blank=True,unique=True)
    description=models.TextField(blank=True,max_length=300)
    image=models.ImageField(upload_to='photos/categories',blank=True)

    def __str__(self):
        return self.category_name
    def get_url(self):
        return reverse('product_categorylist',kwargs={"slug":self.slug})