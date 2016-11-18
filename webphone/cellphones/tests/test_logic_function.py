import datetime
from django.utils import timezone
from django.test import TestCase
from ..models import Producer


class ProducerMethodTests(TestCase):
     
    def test_was_startup_company(self):
        """was_startup_company() should return False for producer whose pub_date is ins the future"""        
        tdate = timezone.now() + datetime.timedelta(days = 30)
        future_producer = Producer(name="HTC",pub_date = tdate.date())
        self.assertEqual(future_producer.was_startup_company(),False)
     
    def test_was_startup_company_wth_old_company(self):
        tdate = timezone.now() + datetime.timedelta(days = -32)
        old_producer = Producer(name='Motorola',pub_date = tdate.date())
        self.assertEqual(old_producer.was_startup_company(), False)
         
         
    def test_was_startup_company_wth_recent_company(self):
        tdate = timezone.now() + datetime.timedelta(hours = -3)        
        recent_producer = Producer(name='My Producer', pub_date = tdate.date())
        self.assertEqual(recent_producer.was_startup_company(), True)
        
    