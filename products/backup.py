from .models import Product
from categories.models import Category
from django.shortcuts import render,get_object_or_404, redirect
#from .forms import CategoryForm
from django.views import generic
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
class CreateProductAuto(LoginRequiredMixin, generic.CreateView):
    model = Product
    template_name = 'products/product_form.html'
    redirect_field_name = 'categories/category_detail.html'
    fields = ['productId','name', 'savePrice','currentPrice','imagePath','updateDate','category']
    vitaminProduct1 = ['43343','test1','12.99','9.12','https://static.chemistwarehouse.com.au/ams/media/pi/55294/hero_150.jpg','2018/01/20 16:22:00']
    #get the category name from Category database
    vitaminCategory = Category.objects.get(name='VITAMINS') 
    if vitaminCategory:
        newProduct = Product(
            productId=vitaminProduct1[0],
            name = vitaminProduct1[1],
            savePrice = vitaminProduct1[2],
            currentPrice = vitaminProduct1[3],
            imagePath = vitaminProduct1[4],
            updateDate = datetime.today(),
            category = vitaminCategory
            )
        newProduct.category = vitaminCategory
        newProduct.save()
    