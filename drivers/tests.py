from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Driver

class DriverTests(APITestCase):
    def test_create_driver(self):
        data = {'name': 'Test Driver', 'email': 'testdr@example.com', 'score': 80}
        response = self.client.post('/drivers/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Driver.objects.count(), 1)
        self.assertEqual(Driver.objects.get().name, 'Test Driver')

    def test_read_driver(self):
        data = {'name': 'Test Driver', 'email': 'testdr@example.com', 'score': 80}
        expected_data = {'url': 'http://testserver/drivers/1/', 'name': 'Test Driver', 'email': 'testdr@example.com', 'score': 80}
        self.client.post('/drivers/', data, format='json')
        response = self.client.get('/drivers/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_update_driver(self):
        data = {'name': 'Test Driver', 'email': 'testdr@example.com', 'score': 80}
        test_data = [
            ({'name': 'new name', 'email': 'testdr@example.com', 'score': 80}, 'name'),
            ({'name': 'Test Driver', 'email': 'newmail@xxx.xx', 'score': 80}, 'email'),
            ({'name': 'Test Driver', 'email': 'testdr@example.com', 'score': 35}, 'score')
        ]

        self.client.post('/drivers/', data, format='json')

        for td in test_data:
            self.client.put('/drivers/1/', td[0], format='json')
            response = self.client.get('/drivers/1/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data[td[1]], td[0][td[1]])

    def test_delete_driver(self):
        data1 = {'name': 'Test Driver #1', 'email': 'testdr1@example.com', 'score': 80}
        data2 = {'name': 'Test Driver #2', 'email': 'testdr2@example.com', 'score': 45}
        self.client.post('/drivers/', data1, format='json')
        self.client.post('/drivers/', data2, format='json')
        self.assertEqual(Driver.objects.count(), 2)
        self.client.delete('/drivers/1/')
        self.assertEqual(Driver.objects.count(), 1)
        self.assertEqual(Driver.objects.get().name, 'Test Driver #2')

    def test_create_driver_blank_fields(self):
        test_data = [
            {'name': 'Test Driver'},
            {'email': 'testdr@example.com'},
            {'score': 80},
            {'email': 'testdr@example.com', 'score': 80},
            {'name': 'Test Driver', 'score': 80},
            {'name': 'Test Driver', 'email': 'testdr@example.com'},
        ]

        for td in test_data:
            response = self.client.post('/drivers/', td, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_non_unique_driver(self):
        initial_driver = {'name': 'Test Driver', 'email': 'testdr@example.com', 'score': 80}
        test_data = [
            {'name': 'Test Driver', 'email': 'testdr@example.com', 'score': 80},
            {'name': 'Test Driver #2', 'email': 'testdr@example.com', 'score': 65}
        ]

        self.client.post('/drivers/', initial_driver, format='json')

        for td in test_data:
            response = self.client.post('/drivers/', td, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
