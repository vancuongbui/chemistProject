from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description','image']
        widgets = {
            'name':forms.TextInput(),
            'description':forms.Textarea(),
            'image':forms.ClearableFileInput(),
        }

        
