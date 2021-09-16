from django import forms

from catalogue.models import Vendor, Product

class VendorCreateForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
