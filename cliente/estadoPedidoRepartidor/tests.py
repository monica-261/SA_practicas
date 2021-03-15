from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from solicitarPedido.models import solicitarPedido

class AccountTests(APITestCase):
    def test_create_pedido(self):
        url = reverse('')
        data = {
            'producto': 'Coca cola',
            'cantidad': '2'
            'precio': 15,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pedido.objects.count(), 1)
