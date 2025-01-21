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
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'category', 'new_category', 'expiry_date']