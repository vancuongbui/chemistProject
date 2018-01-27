from django.shortcuts import render,get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm
from django.views import generic
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from products.models import Product

# Create class CreateView
class CreateCategoryView(LoginRequiredMixin, generic.CreateView):
    form_class = CategoryForm
    model = Category
    template_name = 'categories/category_form.html'
    redirect_field_name = 'categories/category_detail.html'
    

    

class CategoryDetail(generic.ListView):
    model = Category
    fields = ['name','slug']
    template_name = 'products/product_list.html'
    context_object_name = 'category'

     
class CategoryList(generic.ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'category_list'
    def get_context_data(self, **kwargs):
        #call super() to implement base context
        context = super().get_context_data(**kwargs)

        #now, adding extra data as wishing:
        #first, count number of objects displaying in template, divide by 2 (number of colmuns)
        allCategories = Category.objects.all()
        totalEntry = allCategories.count()
        if (totalEntry % 2) == 0:
            totalEntry = (totalEntry // 2)
        else:
            totalEntry = (totalEntry // 2) + 1
        
        #crate a two dimention list to contain objects
        
        listObjects = []
        for i in range(totalEntry): #number of rows displaying in template
            rowEntries = []
            for j in range(2):  #each row contain 2 entries or 2 columns
                try:
                    if allCategories[2*i+j]:
                        rowEntries.append(allCategories[2*i+j])
                    else:
                        pass
                except:
                    pass
            listObjects.append(rowEntries)     
        #pass the list to the context     
        context['listObjects'] = listObjects
        return context


    
