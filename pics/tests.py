from django.test import TestCase
from .models import  Location, Category, Picture

# Create your tests here.


class LocationTestClass(TestCase):
    def setUp(self):
        self.new_location=Location(place='Nairobi')

    def test_category_instance(self):
        self.assertTrue(isinstance(self.new_location, Location))

    def save_location(self):
        before = Location.objects.count()
        self.new_location.save_location()
        after = Location.objects.count()
        self.assertTrue(before < after)

    def tearDown(self):
        Location.objects.all().delete()

class TestCategory(TestCase):
    def setUp(self):
        self.new_category = Category(name='poisonous plants')

    def test_category_instance(self):
        pass

    def test_save_category(self):
        before = Category.objects.count()
        self.new_category.save_category()
        after = Category.objects.count()
        self.assertTrue(before < after)


    def tearDown(self):
        Category.objects.all().delete()

class TestImage(TestCase):
    def setUp(self):
        self.category = Category(name='poisonous plants')
        self.category.save()

        self.location = Location(place='Nairobi')
        self.location.save_location()

        self.new_picture = Picture(name='poisonous plants ', description='Chickweed plants are entirely edible and all its parts can be consumed.', category=self.category)

    def test_picture_instance(self):
        self.assertTrue(isinstance(self.new_picture, Picture))

    def test_picture_update(self):
        pass

    def test_picture_id(self):
        pass

    def test_search_picture(self):
        pass

    def test_save_picture(self):
        before = Picture.objects.count()
        self.new_picture.save_Picture()
        after = Picture.objects.count()
        self.assertTrue(before < after)

    def test_search_by_title(self):
        pass

    def tearDown(self):
        Picture.objects.all().delete()


