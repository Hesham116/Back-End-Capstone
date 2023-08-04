from django.test import TestCase
from restaurant.models import MenuItem, Booking
from restaurant.views import MenuItemsView, SingleItemView, BookingViewSet



class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(name='Item 1', description='Description 1')
        MenuItem.objects.create(name='Item 2', description='Description 2')
        MenuItem.objects.create(name='Item 3', description='Description 3')

    def test_getall(self):
        menus = MenuItem.objects.all()
        self.assertEqual(menus.count(), 3)