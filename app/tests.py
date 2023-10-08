from django.test import TestCase
from django.urls import reverse
from .models import MenuModel


class MenuTestCase(TestCase):
    def setUp(self):
        self.menu = MenuModel.objects.create(name='Menu', named_url='menu', parent=None)

    def test_menu_view(self):
        url = reverse('menu', args=['menu'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
        self.assertIn('tree', response.context)

    def test_menu_hierarchy(self):
        child_menu = MenuModel.objects.create(name='Child Menu', named_url='child-menu', parent=self.menu)
        url = reverse('menu', args=['menu'])
        response = self.client.get(url)

        self.assertContains(response, self.menu.name)
        self.assertContains(response, child_menu.name)
        self.assertContains(response, '<ul class="children">')
