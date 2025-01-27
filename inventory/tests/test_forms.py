from django.test import TestCase
from django.contrib.auth.models import User
from inventory.forms import UserRegisterForm, InventoryItemForm
from inventory.models import Category, InventoryItem

class UserRegisterFormTest(TestCase):
    def test_valid_form(self):
        """Test form is valid with proper input"""
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'ComplexPass123!',
        }
        form = UserRegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_password_mismatch(self):
        """Test form is invalid if passwords don't match"""
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'ComplexPass123!',
            'password2': 'DifferentPass123!',
        }
        form = UserRegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

class InventoryItemFormTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Dairy')

    def test_valid_form(self):
        """Test form is valid with proper input"""
        form_data = {
            'name': 'Milk',
            'quantity': 1.0,
            'unit': 'l',
            'category': self.category.id,
            'expiry_date': '2025-02-01'
        }
        form = InventoryItemForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_quantity_out_of_bounds(self):
        """Test form is invalid if quantity is out of bounds"""
        form_data = {
            'name': 'Milk',
            'quantity': -1,
            'unit': 'l',
            'category': self.category.id,
            'expiry_date': '2025-02-01'
        }
        form = InventoryItemForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors)

        form_data['quantity'] = 1001
        form = InventoryItemForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors)

    def test_invalid_form_both_category_and_new_category(self):
        """Test form is invalid if both category and new_category are provided"""
        form_data = {
            'name': 'Milk',
            'quantity': 1.0,
            'unit': 'l',
            'category': self.category.id,
            'new_category': 'New Category',
            'expiry_date': '2025-02-01'
        }
        form = InventoryItemForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_category', form.errors)
