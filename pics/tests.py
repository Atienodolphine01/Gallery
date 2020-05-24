from django.test import TestCase
from .models import  Location, Category, Picture

# Create your tests here.


class LocationTestClass(TestCase):
    def setUp(self):
        self.new_location=Location(place='Nairobi')

    def test_save_location_method(self):
        self.new_location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location))

    def test_update_location_method(self):
        self.new_location.save_location()
        updated_location = Location.updated_location(self.new_location.id,'Kenya')
        self.assertEqual(updated_location.location, 'Kenya')

    def test_delete_location_method(self):
        self.new_location.save_location()
        self.new_location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

