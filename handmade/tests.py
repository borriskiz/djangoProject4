from django.test import TestCase
from django.urls import reverse

from handmade import factories, models


class HandmadeTestCase(TestCase):
    def setUp(self):
        self.item = factories.HandmadeItemFactory()

    def test_get_item_list(self):
        url = reverse('handmade_item_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['items'].count(), models.HandmadeItem.objects.count())

    def test_detail_view(self):
         url = reverse('handmade_item_detail', kwargs={'pk': self.item.pk})
         response = self.client.get(url)
         self.assertEqual(response.status_code, 200)

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
            'image': self.item.image,
            'materials': [factories.MaterialFactory().pk, factories.MaterialFactory().pk],
        }

        response = self.client.post(url, data)

        if response.status_code == 200:
            print(response.context['form'].errors)

        self.item.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(self.item.name, old_name)
