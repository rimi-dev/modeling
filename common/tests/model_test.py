from django.test import TestCase
from common.models import (Car, Company, CompanyCarCount, Customer, RequestHouseMove, MoveFeedback)


class CompanyRelationModelTestCase(TestCase):
    def setUp(self):
        self.car = Car(weight='1톤')
        self.car.save()
        self.old_count = Company.objects.count()
        self.company = Company(name='(주)마켓디자이너스', owner_name='김현영', tel='025180060', address='서울 강남구 역삼동 736-17',
                               registration_number='1234567890', registration_date='2020-01-01', workers_count=100,
                               is_matching=True)
        self.company.save()
        self.one_car_count = CompanyCarCount(car=self.car, count=20, company=self.company)

    def test_model_can_create_a_company(self):
        self.one_car_count.save()
        self.company.cars_count.add(self.car)
        self.company.save()
        new_count = Company.objects.count()
        self.assertNotEqual(self.old_count, new_count)

    def test_model_can_update_a_company(self):
        old_car_count = CompanyCarCount.objects.count()
        self.one_car_count.count = 93
        self.one_car_count.save()
        self.company.workers_count = 88
        self.company.save()
        new_car_count = CompanyCarCount.objects.count()
        self.assertEqual(old_car_count, new_car_count)
        self.assertEqual(self.old_count, Company.objects.count())
        self.assertTrue(self.company.workers_count == 88)
        self.assertTrue(self.one_car_count.count == 93)


class CustomerRelationModelTestCase(TestCase):
    def setUp(self):
        self.customer_count = Customer.objects.count()
        self.request_count = RequestHouseMove.objects.count()

    def test_customer_can_request_move_house(self):
        customer = Customer(name='김예림', tel='01074071803', joined_date='2020-01-03', is_agree_terms=True,
                            is_agree_marketing=True, is_agree_third_party=True)
        customer.save()

        request_house = RequestHouseMove(customer=customer, starting_floors='19층', starting_address='경기도 안양시 관양동',
                                         destination_floors='25층 이상', destination_address='서울시 강남구 역삼동',
                                         move_date='2020-09-01', is_storage=False)
        request_house.save()
        self.assertNotEqual(self.customer_count, Customer.objects.count())
        self.assertNotEqual(self.request_count, RequestHouseMove.objects.count())


class FeedbackModelTestCase(TestCase):
    def setUp(self):
        self.count = MoveFeedback
        self.company = Company(name='(주)마켓디자이너스', owner_name='김현영', tel='025180060', address='서울 강남구 역삼동 736-17',
                               registration_number='1234567890', registration_date='2020-01-01', workers_count=100,
                               is_matching=True)
        self.company.save()

    def test_model_can_create_a_feedback(self):
        feedback = MoveFeedback(company=self.company, is_agree_public=True, professional_level=3, price_level=5,
                                kindness_level=2, is_revisit=True, contract_price=3000000, move_date='2020-01-03',
                                content='''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
                                tempor incididunt ut labore et dolore magna aliqua. Nisl tincidunt eget nullam non.
                                Quis hendrerit dolor magna eget est lorem ipsum dolor sit. Volutpat odio facilisis 
                                mauris sit amet massa. Commodo odio aenean sed adipiscing diam donec adipiscing 
                                tristique. Mi eget mauris pharetra et. Non tellus orci ac auctor augue. 
                                Elit at imperdiet dui accumsan sit. Ornare arcu dui vivamus arcu felis. 
                                Egestas integer eget aliquet nibh praesent. In hac habitasse platea dictumst quisque 
                                sagittis purus. Pulvinar elementum integer enim neque volutpat ac.''')

        feedback.save()
        self.assertNotEqual(self.count, MoveFeedback.objects.count())
