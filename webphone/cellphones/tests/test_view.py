import datetime

from django.utils import timezone
from django.core.urlresolvers import reverse
from django.test import TestCase
from ..models import Producer, Smartphone


def create_smartphone(phone_model, days, producer_name="Apple"):
    """Create a smartphone with given phone_model"""
    time = timezone.now() + datetime.timedelta(days = days)    
    try:        
        p = Producer.objects.get(name=producer_name)        
    except Producer.DoesNotExist:
        p = Producer.objects.create(name=producer_name, pub_date=datetime.datetime(2010,1,1))        
    return Smartphone.objects.create(phone_model=phone_model,pub_date=time.date(), producer=p)
    
        
class SmartphoneViewTest(TestCase):
    
#     def setUp(self):
#         super(SmartphoneViewTest, self).setUp()
#          
#         # start with empty database of smartphone
#         Smartphone.objects.all().delete()

     
    def test_index_view_wth_no_phones(self):
         
        """If no question exist, appropriate should be displayed"""
        Smartphone.objects.all().delete()
        response = self.client.get(reverse('cellphones:index'))    
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No phones are available.")
        self.assertQuerysetEqual(response.context["smartphone_list"],[])        
            
    def test_index_view_with_a_past_smartphone(self):        
        create_smartphone("Iphone 4", -30)        
        response = self.client.get(reverse('cellphones:index'))                
        self.assertContains(response,"Iphone 4",status_code=200)        
        self.assertQuerysetEqual(
                response.context['smartphone_list'],
                ["<Smartphone: Iphone 4  (by Apple)>"])
        
        
    def test_index_view_with_a_future_smartphone(self):

        create_smartphone("Iphone 7", 30)
        response = self.client.get(reverse('cellphones:index'))
        self.assertContains(response,"No phones are available.", status_code=200)
        self.assertQuerysetEqual(
                response.context['smartphone_list'],
                [])
         
    def test_index_view_with_past_and_future_smartphone(self):
        
        create_smartphone("Iphone 4", -30)
        create_smartphone("Iphone 7", 30)
        response = self.client.get(reverse('cellphones:index'))        
        self.assertQuerysetEqual(
                response.context['smartphone_list'],
                ["<Smartphone: Iphone 4  (by Apple)>"])
         
    def test_index_view_with_two_past_smartphone(self):
        
        create_smartphone("Iphone 4", -30)
        create_smartphone("Iphone 5", -15)  # newest
        response = self.client.get(reverse('cellphones:index'))
        #self.assertContains(response,"No phones are available.", status_code=200)
        self.assertQuerysetEqual(
                response.context['smartphone_list'],
                ["<Smartphone: Iphone 5  (by Apple)>","<Smartphone: Iphone 4  (by Apple)>"])    
        #order by -pub_date
        
        
class SmartphoneDetailViewTests(TestCase):    
    def test_detail_view_wth_future_smartphone(self):
        future_smartphone = create_smartphone("iPhone 7", 10)
        response = self.client.get(reverse('cellphones:detail',
                                           args = (future_smartphone.id,)))
        self.assertEqual(response.status_code,404)        
    
    def test_detail_view_wth_past_smartphone(self):
        past_smartphone = create_smartphone(phone_model = "iPhone 2",days = -120)
        response = self.client.get(reverse('cellphones:detail',
                                           args = (past_smartphone.id,)))
        self.assertContains(response, past_smartphone.phone_model, status_code=200)        
    