from django.test import TestCase
from model_mommy import mommy
from common.models import (Car, Company, CompanyCarCount, Customer, RequestHouseMove, MoveFeedback)


class CompanyRelationModelTestCase(TestCase):
    def setUp(self):
        self.old_count = Company.objects.count()
        self.car = mommy.make(Car)
        self.company = mommy.make(Company, make_m2m=True)
        self.one_car_count = mommy.make(CompanyCarCount)

    def test_relation_can_create_a_company(self):
        self.company.cars_count.add(self.car)
        self.company.save()
        new_count = Company.objects.count()
        self.assertNotEqual(self.old_count, new_count)

    def test_relation_can_update_a_company(self):
        old_car_count = CompanyCarCount.objects.count()
        old_company_count = Company.objects.count()
        self.one_car_count.count = 93
        self.one_car_count.save()
        self.company.workers_count = 88
        self.company.save()
        new_car_count = CompanyCarCount.objects.count()
        self.assertEqual(old_car_count, new_car_count)
        self.assertEqual(old_company_count, Company.objects.count())
        self.assertTrue(self.company.workers_count == 88)
        self.assertTrue(self.one_car_count.count == 93)


class CustomerRelationModelTestCase(TestCase):
    def setUp(self):
        self.customer_count = Customer.objects.count()
        self.request_count = RequestHouseMove.objects.count()
        self.customer = mommy.make(Customer)
        self.request_house = mommy.make(RequestHouseMove, customer=self.customer)

    def test_relation_can_update_a_customer(self):
        old_count = RequestHouseMove.objects.filter(customer__name='홍길동').count()
        self.customer.name = '홍길동'
        self.customer.save()
        new_count = RequestHouseMove.objects.filter(customer__name='홍길동').count()
        self.assertNotEqual(old_count, new_count)


class FeedbackModelTestCase(TestCase):
    def setUp(self):
        self.count = MoveFeedback.objects.count()
        self.company = mommy.make(Company)
        self.feedback = mommy.make(MoveFeedback, company=self.company)

    def test_relation_can_update_a_feedback(self):
        old_count = MoveFeedback.objects.filter(company__name='테스트컴퍼니').count()
        self.company.name = '테스트컴퍼니'
        self.company.save()
        new_count = MoveFeedback.objects.filter(company__name='테스트컴퍼니').count()
        self.assertNotEqual(old_count, new_count)
