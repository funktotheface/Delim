from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from inventory.models import InventoryItem, Category
from django.core.exceptions import ValidationError

class InventoryItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.category = Category.objects.create(name='Dairy')
        self.inventory_item = InventoryItem.objects.create(
            name='Milk',
            quantity=2.5,
            unit='l',
            category=self.category,
            expiry_date=date(2025, 2, 1),
            user=self.user
        )

    def test_string_representation(self):
        """Test the string representation of InventoryItem"""
        self.assertEqual(str(self.inventory_item), 'Milk')

    def test_default_unit(self):
        """Test the default unit is 'u' (unit)"""
        item = InventoryItem.objects.create(
            name='Butter',
            quantity=1.0,
            user=self.user
        )
        self.assertEqual(item.unit, 'u')

    def test_quantity_validation(self):
        """Test that quantity cannot be less than 0 or greater than 1000"""
        with self.assertRaises(ValidationError):
            InventoryItem.objects.create(name='Negative Test', quantity=-1, user=self.user).full_clean()
        with self.assertRaises(ValidationError):
            InventoryItem.objects.create(name='Excess Test', quantity=1001, user=self.user).full_clean()

    def test_category_relationship(self):
        """Test the relationship between InventoryItem and Category"""
        self.assertEqual(self.inventory_item.category.name, 'Dairy')

    def test_expiry_date_can_be_null(self):
        """Test that expiry_date can be null"""
        item = InventoryItem.objects.create(
            name='Cheese',
            quantity=1.5,
            unit='kg',
            category=self.category,
            expiry_date=None,
            user=self.user
        )
        self.assertIsNone(item.expiry_date)


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Fruits")

    def test_string_representation(self):
        """Test the string representation of Category"""
        self.assertEqual(str(self.category), "Fruits")

    def test_unique_name(self):
        """Test that Category names must be unique"""
        with self.assertRaises(Exception):
            Category.objects.create(name="Fruits")

    def test_plural_verbose_name(self):
        """Test that verbose_name_plural is 'Categories'"""
        self.assertEqual(Category._meta.verbose_name_plural, "Categories")
