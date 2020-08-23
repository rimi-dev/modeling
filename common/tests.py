from django.test import TestCase
from common.models import Car


class CarModelTestCase(TestCase):
    def setUp(self):
        self.car_weight = '1톤'
        self.car = Car(weight=self.car_weight)

    def test_model_can_create_a_car(self):
        old_count = Car.objects.count()
        self.car.save()
        new_count = Car.objects.count()
        self.assertNotEqual(old_count, new_count)