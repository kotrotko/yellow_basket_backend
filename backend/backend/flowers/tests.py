from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from backend.flowers.models import Flower

class FlowerListViewTest(TestCase):
    def setUp(self):
        # Create some sample Flower data
        Flower.objects.create(sort='Tulip', color='red', price=10.5, stock=100)
        Flower.objects.create(sort='Rose', color='white', price=5.0, stock=100)
        self.client = APIClient()

    def test_flower_list(self):
        # Make a GET request to the FlowerListView
        response = self.client.get('/api/flowers/')

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the correct data is returned
        flowers = Flower.objects.all()
        expected_data = [
            {
                'sort': flower.sort,
                'color': flower.color,
                'price': str(flower.price),
                'stock': flower.stock,
            } for flower in flowers
        ]

        self.assertEqual(response.json(), expected_data)


class FlowerAPITestCase(APITestCase):

    def setUp(self):
        # Create a test flower in the database
        self.flower = Flower.objects.create(sort="Tulip", price=2.50, color="Red", stock=100)

        # Define API endpoint URLs
        self.list_url = reverse("flower_list_api")  # Match URL name from urls.py
        self.detail_url = reverse("flower_detail_api", args=[self.flower.id])

    def test_get_flower_list(self):
        """Test retrieving the list of flowers."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_flower(self):
        """Test creating a new flower via POST request."""
        data = {"sort": "Rose", "price": 3.00, "color": "White", "stock": 50}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_flower_detail(self):
        """Test retrieving details of a specific flower."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
