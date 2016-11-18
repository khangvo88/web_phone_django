from django.db import models


#from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.utils import timezone
import datetime, os
from .helpers import device_image_upload_to

from image_cropping import ImageCropField, ImageRatioField

# Create your models here.
STATUS_ACTIVE = 1
STATUS_INACTIVE = 2
STATUS_CLOSED = 3
STATUS_CHOICES = (
        (STATUS_ACTIVE,'ACTIVE'),
        (STATUS_INACTIVE,'INACTIVE'),
        (STATUS_CLOSED,'CLOSED'),
    )

class Producer(models.Model):
    
    name = models.CharField(max_length=100)
    pub_date = models.DateField('published on',blank=True, null=True, default=datetime.date(2010,1,1))
    email = models.EmailField(max_length=254, default='', blank=True)
    description = models.CharField(max_length=1000, blank=True)    
    
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
            
    def __str__(self):
        return self.name
            
    
class DeviceAccessories(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, default="",blank=True) 
    TYPE_IN_ACCESSORIES =(
        ('ADAPTER'      , "Adapter"),
        ('HEADPHONE'    , "Headphone"),
        ('MANUAL'       , "Manual book"),
        ('CORD'         , "Chargin cord"),
        ('OTHERS'         , "Others"), 
    )    
    type = models.CharField(max_length=10, choices = TYPE_IN_ACCESSORIES,
                            default="Adapter")        
    price = models.FloatField(default=0)            
    def __str__(self):
        return "%s %s" %(self.producer.name, self.name)
    
# class DeviceCategories(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return "%s" %self.name
#     
#     

class CommonSpecification(models.Model):        
    screen          = models.CharField(max_length=100,blank=True, null=True)
    os              = models.CharField(max_length=100,blank=True, null=True)
    camera_front    = models.CharField(max_length=100,blank=True, null=True)    
    cpu             = models.CharField(max_length=100,blank=True, null=True)
    ram             = models.CharField(max_length=100,blank=True, null=True)    
    internal_memory = models.CharField(max_length=100,blank=True, null=True)
    memory_card     = models.CharField(max_length=100,blank=True, null=True)    
    wireless_tech   = models.CharField(max_length=100,blank=True, null=True)
    battery         = models.CharField(max_length=100,blank=True, null=True)
    color           = models.CharField(max_length=100, blank=True, null=True)
    weight          = models.FloatField(blank=True, default=0, null=True)    
    
    # LAPTOP only
    com_port        = models.CharField(max_length=100,blank=True, null=True)    
    connection_type = models.CharField(max_length=100,blank=True, null=True)
    harddisk        = models.CharField(max_length=100,blank=True, null=True)
    gpu             = models.CharField(max_length=100,blank=True, null=True)
    optical_disk    = models.CharField(max_length=100,blank=True, null=True)
    webcam          = models.CharField(max_length=100,blank=True, null=True)
    
    # SMARTPHONE/TABLET only 
    sim_type        = models.CharField(max_length=100,blank=True, null=True)
    camera_back     = models.CharField(max_length=100,blank=True, null=True)
    design          = models.CharField(max_length=100,blank=True, null=True)
    
    special_features= models.TextField(max_length=100,blank=True, null=True)
    
    class Meta:
        abstract = True      
    
class Device(CommonSpecification):
    DEVICE_SMARTPHONE = 1
    DEVICE_TABLET = 2
    DEVICE_LAPTOP = 3 
    DEVICE_CATEGORIES_CHOICES = ((DEVICE_SMARTPHONE,'SMARTPHONE'),
                                 (DEVICE_TABLET,'TABLET'),
                                 (DEVICE_LAPTOP,'LAPTOP')
                                )
    
    DEVICE_CONDITION_NEW        = 1
    DEVICE_CONDITION_LIKENEW    = 2
    DEVICE_CONDITION_USED       = 3
    DEVICE_CONDITION_REFURBRISH = 4
    DEVICE_CONDITION_CHOICES = ((DEVICE_CONDITION_NEW,'NEW'),
                                 (DEVICE_CONDITION_LIKENEW,'LIKE NEW'),
                                 (DEVICE_CONDITION_USED,'USED'),
                                 (DEVICE_CONDITION_REFURBRISH,'REFURBRISH')
                                )
    
    category = models.SmallIntegerField(choices=DEVICE_CATEGORIES_CHOICES,default=DEVICE_SMARTPHONE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)    
    name = models.CharField(max_length=100)    
    model = models.CharField(max_length=100, blank=True)            
    description = models.TextField(max_length=500,blank=True)
    price = models.FloatField(default=0)    # original-price
    price_1 = models.FloatField(default=0, verbose_name='New price')  # discount-price    
    
    is_featured = models.BooleanField(verbose_name="Featured Product",default=False)
    on_sale = models.BooleanField(verbose_name='On Sale', default=False)
    pub_date = models.DateField('date published',blank=True,null=True)
    condition = models.SmallIntegerField(choices=DEVICE_CONDITION_CHOICES,
                                        default=DEVICE_CONDITION_NEW)    
    warranty = models.IntegerField(default=12)   #default warranty = 12 month
    accessories = models.ManyToManyField(DeviceAccessories,through='DeviceAndAccessories')
                
    # META-DATA
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO: add reviews component

    #device_image = models.ImageField(upload_to=device_image_upload_to, null=True)
    device_image = models.ImageField(upload_to="raw", null=True)
    image_ratio = ImageRatioField('device_image','241x212')

    
    class Meta:
        ordering = ['pub_date', 'name']     
        
    def __str__(self):
        # return "%s: %s %s" %(self.DEVICE_CATEGORIES_CHOICES[1+self.category][1],
        #                     self.producer.name, self.name)
        return "%s %s" %(self.producer.name, self.name)

    def get_fullname(self):
        temp =  "%s %s %s" % (self.producer.name.title(), self.name, self.model)
        return temp.strip(' \t\n\r')

    def is_new_product(self, DAY_DIFF=7):
        """return True if it created within 1 week"""
        return self.created_at >= timezone.now() - datetime.timedelta(days=DAY_DIFF)
        pass

    @staticmethod
    def list_category():
        return dict(Device.DEVICE_CATEGORIES_CHOICES)

    @staticmethod
    def condition_status(value):
        try:
            return Device.DEVICE_CONDITION_CHOICES[value-1][1]
        except:
            return None


# class DeviceImages(models.Model):
#     text = models.TextField(max_length=100, blank=True, null=True)
#     img_url = models.ImageField()
#     image_desc = models.CharField(max_length=200, blank=True, nul=True)
         
class DeviceAndAccessories(models.Model):
    device = models.ForeignKey(Device)
    accessories = models.ForeignKey(DeviceAccessories)
    is_integrated = models.BooleanField(default=False)
    
