import os

from django.test import TestCase
from django.urls import reverse

from handmade import factories, models


class HandmadeTestCase(TestCase):
    def setUp(self):
        self.item = factories.HandmadeItemFactory()
        self.material = factories.MaterialFactory()

    def tearDown(self):
        if self.item.image:
            image_path = self.item.image.path
            print(image_path)
            if os.path.isfile(image_path):
                os.remove(image_path)

    def test_list_view(self):
        url = reverse('handmade_item_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['items'].count(), models.HandmadeItem.objects.count())

    def test_detail_view(self):
        url = reverse('handmade_item_detail', kwargs={'pk': self.item.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['item'], self.item)

    def test_delete_view(self):
        url = reverse('handmade_item_delete', kwargs={'pk': self.item.pk})
        old_items_count = models.HandmadeItem.objects.count()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertGreater(old_items_count, models.HandmadeItem.objects.count())

    def test_update_view(self):
        url = reverse('handmade_item_update', kwargs={'pk': self.item.pk})
        old_name = self.item.name
        data = {
            'name': 'new_name',
            'price': self.item.price,
            'item_type': self.item.item_type.pk,
            'market': self.item.market.pk,
            'date_receipt': self.item.date_receipt,
            'materials': [factories.MaterialFactory().pk, factories.MaterialFactory().pk],
        }

        response = self.client.post(url, data)

        if response.status_code == 200:
            print(response.context['form'].errors)

        self.item.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(self.item.name, old_name)

    def test_create_view(self):
        url = reverse('handmade_item_create')
        old_items_count = models.HandmadeItem.objects.count()
        new_name = 'new_item'
        new_price = 100
        new_date_receipt = '2024-10-21'

        data = {
            'name': new_name,
            'price': new_price,
            'item_type': factories.ItemTypeFactory().pk,
            'market': factories.MarketFactory().pk,
            'date_receipt': new_date_receipt,
            # 'image': None,
            'materials': [self.material.pk],
        }

        response = self.client.post(url, data)
        if response.status_code == 200:
            print(response.context['form'].errors)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.HandmadeItem.objects.count(), old_items_count + 1)

        created_item = models.HandmadeItem.objects.latest('id')
        self.assertEqual(created_item.name, new_name)
        self.assertEqual(created_item.price, new_price)
        self.assertEqual(str(created_item.date_receipt), new_date_receipt)
        self.assertEqual(created_item.item_type.pk, data['item_type'])
        self.assertEqual(created_item.market.pk, data['market'])
        self.assertEqual(list(created_item.materials.values_list('pk', flat=True)), data['materials'])
