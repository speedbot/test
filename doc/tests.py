import json

from django.test import TestCase
from django.test import Client
from django.urls import reverse

from .models import Document
from .forms import DocumentForm
from .factories import StaffUerFactory


class TestApi(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = StaffUerFactory.create()

    def get_data(self):
        kwargs = {
            'owner': self.user,
            'type': 'type',
            'source_type': '.txt',
            'source_id': '1',
        }
        return kwargs

    def test_models(self):
        self.assertEqual(Document.objects.count(), 0)
        Document.objects.create(
            **self.get_data(),
        )
        self.assertEqual(Document.objects.count(), 1)

    def test_form(self):
        data = self.get_data()
        data['owner'] = self.user.id
        form = DocumentForm(data)
        self.assertEqual(form.is_valid(), True)
        data.pop('owner')
        form = DocumentForm(data)
        self.assertEqual(form.is_valid(), False)

    def test_get(self):
        url = reverse('api:document-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        document = Document.objects.create(
            **self.get_data(),
        )
        self.assertEqual(Document.objects.count(), 1)
        url = reverse('api:document-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        document = Document.objects.create(
            **self.get_data(),
        )
        url = reverse('api:document-detail', args=(document.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        document = Document.objects.create(
            **self.get_data(),
        )
        url = reverse('api:document-detail', args=(document.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_create(self):
        data = self.get_data()
        data['user_id'] = self.user.id
        url = reverse('api:document-list')
        self.assertEqual(Document.objects.count(), 0)
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Document.objects.count(), 1)