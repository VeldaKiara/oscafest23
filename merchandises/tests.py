from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Merchandise

class MerchandiseAPITestCase(TestCase):
    def setUp(self):
        self.merchandise = Merchandise.objects.create(name='Test Merchandise', price=10.99)
        self.merchandise_list_url = reverse('merchandises:merchandise-list')
        self.merchandise_detail_url = reverse('merchandises:merchandise-detail', args=[self.merchandise.pk])

    def test_get_all_merchandises(self):
        response = self.client.get(self.merchandise_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_merchandise(self):
        response = self.client.get(self.merchandise_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_merchandise(self):
        data = {'name': 'New Merchandise', 'price': 19.99}
        response = self.client.post(self.merchandise_list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_merchandise(self):
        data = {'name': 'Updated Merchandise', 'price': 15.99}
        response = self.client.put(self.merchandise_list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_merchandise(self):
        response = self.client.delete(self.merchandise_list_url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
