from django.forms import ModelForm
from django import forms
from apps.productmodule.models import Product,Category


class ProductForm (ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    name = forms.CharField()
    price = forms.IntegerField()
    quantity = forms.IntegerField()
    category = forms.ModelChoiceField(label='catogory',queryset=Category.objects.all())
    
    
    
    
    
    
    
    

    
    
    






