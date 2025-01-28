from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import InventoryItem, Category

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class InventoryItemForm(forms.ModelForm):
    new_category = forms.CharField(required=False, label='New Category')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Existing Category')
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True, label='Expiry Date') 
    unit = forms.ChoiceField(choices=InventoryItem.UNIT_CHOICES, label='Unit')

    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'unit', 'category', 'new_category', 'expiry_date']

    def clean(self):
        cleaned_data = super().clean()
        new_category_name = cleaned_data.get('new_category')
        category = cleaned_data.get('category')
        quantity = cleaned_data.get('quantity')

        if new_category_name and category:
            self.add_error('new_category', 'Please provide either an existing category or a new category, not both.')

        if quantity is not None and (quantity < 0 or quantity > 1000):
            self.add_error('quantity', 'Quantity must be between 0 and 1000')

        if new_category_name:
            if Category.objects.filter(name=new_category_name).exists():
                self.add_error('new_category', 'Category with this name already exists.')

        return cleaned_data