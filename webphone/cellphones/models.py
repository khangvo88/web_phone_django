from django.db import models
import datetime


# Create your models here.

class Producer(models.Model):
    name = models.TextField(max_length=100)
    pub_date = models.DateField('date created')
    email = models.EmailField(max_length=254, default='')
    description = models.TextField(max_length=200, blank=True)
        
    def __str__(self):
        return self.name
    
    def was_startup_company(self):
        return self.pub_date >= datetime.date.today() - datetime.timedelta(days=30)
    was_startup_company.admin_order_field = 'pub_date'
    was_startup_company.boolean = True
    was_startup_company.short_description = 'Start-up company?'        
     

class Smartphone(models.Model):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)    
    phone_model = models.CharField(max_length=50)        
    pub_date = models.DateField('date published')
    description = models.TextField(max_length=200,blank=True)    
    price = models.FloatField(default=0)
    total_sales = models.IntegerField(default=0)
    
    
    def __str__(self):
        return "%s  (by %s)" %(self.phone_model,self.producer.name)