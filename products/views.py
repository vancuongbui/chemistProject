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
from django.shortcuts import render
from django.db.models import Count
from math import *

# Create your views here.
class CreateProductView(LoginRequiredMixin, generic.CreateView):
    model = Product
    template_name = 'products/product_form.html'
    redirect_field_name = 'categories/category_detail.html'
    fields = ['productId','name','currentPrice','savePrice','imagePath','updateDate','category']

class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'product_list'
    select_related = ('category')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(category__slug__iexact = self.kwargs.get('slug'))
    #override the get_context_data to add extra data to the templates
    #the purpose is to simplify the html structure
    def get_context_data(self, **kwargs):
        
        #call super() to implement base context
        context = super().get_context_data(**kwargs)

        #now, adding extra data as wishing:
        #first, count number of objects displaying in template, divide by 2 (number of colmuns)
        totalEntry = Product.objects.filter(category__slug__iexact = self.kwargs.get('slug')).count()
        if (totalEntry % 2) == 0:
            totalEntry = (totalEntry // 2)
        else:
            totalEntry = (totalEntry // 2) + 1
        
        #crate a two dimention list to contain objects
        allProducts = list(Product.objects.filter(category__slug__iexact = self.kwargs.get('slug')).all())
        listObjects = []
        for i in range(totalEntry):
            rowEntries = []
            for j in range(2):
                try:
                    if allProducts[2*i+j]:   
                        if allProducts[2*i+j].discount() > 0.2:                   
                            rowEntries.append(allProducts[2*i+j])
                    else:
                        pass
                except:
                    pass
            listObjects.append(rowEntries)     
        #pass the list to the context     
        context['listObjects'] = listObjects
        return context
        


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        
        #call super() to implement base context (object)
        context = super().get_context_data(**kwargs)

        #, then add extra context to the above context
        context['testContext'] = 'This is the test of additional context'
        return context

    



