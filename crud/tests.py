from cgi import test
from http import client
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product,Bill,Client,Bills_Product


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        testuser1.save()

        test_client = Client.objects.create(
            document = '1192812328', first_name = 'eduardo', last_name = 'bonet',email = 'bonet@gmail.com', User= testuser1)
        test_client.save()

        test_bill = Bill.objects.create(client_id = 1, company_name ='google', nit = '987654321',code = '4567')
        test_bill.save()
        #test_product = 

    def test_client_content(self):
        
        client = Client.objects.get(id=1)
        document = f'{client.document}'
        first_name = f'{client.first_name}'
        last_name = f'{client.last_name}'
        email = f'{client.email}'
        user = f'{client.User}'
        self.assertEqual(document, '1192812328')
        self.assertEqual(first_name, 'eduardo')
        self.assertEqual(last_name, 'bonet')
        self.assertEqual(email, 'bonet@gmail.com')
        self.assertEqual(str(user), "test_user1")
        self.assertEqual(str(client), "1 - eduardo bonet")

    def test_bill_content(self):
        
        bill = Bill.objects.get(id=1)
        client_id = f'{bill.client_id}'
        company_name = f'{bill.company_name}'
        nit = f'{bill.nit}'
        code = f'{bill.code}'
        
        self.assertEqual(client_id, '1 - eduardo bonet')
        self.assertEqual(company_name, 'google')
        self.assertEqual(nit, '987654321')
        self.assertEqual(code, '4567')
        self.assertEqual(str(bill), "1 - google")
        