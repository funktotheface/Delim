from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, timedelta, date
from inventory.models import InventoryItem, Category

class ItemDetailsViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.category = Category.objects.create(name="Dairy")
        self.item = InventoryItem.objects.create(
            name="Milk",
            quantity=1.0,
            unit="l",
            category=self.category,
            expiry_date="2025-02-01",
            user=self.user
        )
        self.client = Client()

    def test_item_details(self):
        """Test JSON response for item details"""
        url = reverse('item-details', args=[self.item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "name": "Milk",
            "quantity": 1.0,
            "unit": "l",
            "category": "Dairy",
            "expiry_date": "2025-02-01",
            "user": self.user.username
        })


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_context(self):
        """Test Index view context with a random quote"""
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('quote', response.context)
        self.assertIn('attributedTo', response.context)


class DashboardViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = Client()
        self.client.login(username="testuser", password="testpass")

    def test_dashboard_context(self):
        """Test Dashboard view context data"""
        today = datetime.now().date()
        InventoryItem.objects.create(
            name="Milk",
            quantity=1.0,
            unit="l",
            expiry_date=today + timedelta(days=2),
            user=self.user
        )
        url = reverse('dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('items', response.context)
        self.assertIn('expiring_items', response.context)


class SignUpViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_get(self):
        """Test GET request for signup form"""
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/signup.html')

    def test_signup_post(self):
        """Test POST request for signup form"""
        url = reverse('signup')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123'
        }
        response = self.client.post(url, data)
        if response.status_code != 302:
            print(response.context['form'].errors)  # Print form errors if the form is not valid
        self.assertEqual(response.status_code, 302)  # Redirect after successful signup
        self.assertTrue(User.objects.filter(username='newuser').exists())


class AddItemViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.category = Category.objects.create(name="Dairy")
        self.client = Client()
        self.client.login(username="testuser", password="testpass")

    def test_add_item_get(self):
        """Test GET request for add item page"""
        url = reverse('add-item')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/add_item.html')

    def test_add_item_post(self):
        """Test POST request for adding an item"""
        url = reverse('add-item')
        data = {
            'name': 'Butter',
            'quantity': 1.0,
            'unit': 'kg',
            'category': self.category.id,
            'expiry_date': '2025-02-01',
            'user': self.user.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful post
        self.assertTrue(InventoryItem.objects.filter(name="Butter").exists())


class EditItemViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.category = Category.objects.create(name="Dairy")
        self.item = InventoryItem.objects.create(
            name="Milk",
            quantity=1.0,
            unit="l",
            category=self.category,
            expiry_date="2025-02-01",
            user=self.user
        )
        self.client = Client()
        self.client.login(username="testuser", password="testpass")

    def test_edit_item_post(self):
        """Test POST request for editing an item"""
        url = reverse('edit-item', args=[self.item.id])
        data = {
            'name': 'Milk',
            'quantity': 2.0,
            'unit': 'l',
            'category': self.category.id,
            'expiry_date': '2025-02-01',
            'user': self.user.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful post
        self.item.refresh_from_db()
        self.assertEqual(self.item.quantity, 2.0)


class DeleteItemViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.item = InventoryItem.objects.create(
            name="Milk",
            quantity=1.0,
            unit="l",
            expiry_date="2025-02-01",
            user=self.user
        )
        self.client = Client()
        self.client.login(username="testuser", password="testpass")

    def test_delete_item(self):
        """Test deleting an item"""
        url = reverse('delete-item', args=[self.item.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Redirect after successful delete
        self.assertFalse(InventoryItem.objects.filter(id=self.item.id).exists())
