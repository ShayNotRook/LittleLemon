from django.test import TestCase, RequestFactory
from restaurant.models import Menu
from restaurant.views import MenuItemView
from restaurant.serializers import MenuSerializer

class MenuItemViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        Menu.objects.create(
            title='Apple Pie',
            price=60,
            inventory=100,
        )
        Menu.objects.create(
            title='Roasted Chicken',
            price=100,
            inventory=100
        )
        
    def test_getall(self):
        menuitems = Menu.objects.all()
        serialized_items = MenuSerializer(menuitems, many=True)
        request = self.factory.get(path='restaurant/menu/')
        response = MenuItemView.as_view()(request)
        
        self.assertEqual(response.data, serialized_items.data)