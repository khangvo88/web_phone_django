from django.contrib import admin
from django.utils import timezone
import datetime

# Register your models here.
#from .models import Device, Producer, Tablet, Smartphone, MobileSpecification, DeviceAccessories
from .models import Producer, Device, DeviceAccessories, CommonSpecification, DeviceAndAccessories

from django.db.models import Count
from image_cropping import ImageCroppingMixin


#class ChoiceInline(admin.StackedInline):
class DeviceInline(admin.TabularInline):
    model = Device
    extra = 1    
    fieldsets = (
        (
            None, 
            {
                'fields': ('name','price','category', 'is_featured')
            }
        ),
    )

    
class AccessoriesInline(admin.TabularInline):
    model = Device.accessories.through
    extra =1
    pass

class AccessoriesAdmin(admin.ModelAdmin):
    inline = [AccessoriesInline,]
    pass    


class ProducerAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        return Producer.objects.annotate(product_count=Count('device'))
            
    fieldsets = [
        (None       ,{'fields':['name']}),
        ('Details',{'fields':['pub_date','email','description'],'classes':['collapse']}),        
    ]
    inlines = [DeviceInline]
    #list_display = ('name','pub_date','was_startup_company')
    list_display = ('name','created_at','was_startup_company', 'show_product_count')
    list_filter =['pub_date']
    search_fields = ['name']
    #date_hierarchy ='pub_date'
    date_hierarchy ='created_at'
    
    def show_product_count(self, inst):
        return inst.product_count
    show_product_count.admin_order_field = 'product_count'
    
    def was_startup_company(self, instance):
        if not instance.pub_date:
            return False
        STARTUP_DAY = 30 #30 days
        return timezone.now().date() >= instance.pub_date >= timezone.now().date() - datetime.timedelta(days=STARTUP_DAY)    
        
    was_startup_company.admin_order_field = 'pub_date'
    was_startup_company.boolean = True
    was_startup_company.short_description = 'Start-up company?'
    
    #list_per_page = 100 #default    
    #list_select_related = ('name','pub_date') #LEARN LATER    
    
    

class DeviceAdmin(ImageCroppingMixin, admin.ModelAdmin):
    
    list_display = ('name','category','price','producer', 'is_featured')
    fieldsets = [
        (None           ,{'fields':['category','producer','name','model', 'price',
                                    'price_1','is_featured','pub_date', 'condition', 'warranty',
                                    'description','device_image','image_ratio','status']}),
        ('Specification',{'fields':CommonSpecification._meta.get_all_field_names(),
                      'classes':['collapse']}),
    ]
    list_filter=['category','producer']
    inlines = [AccessoriesInline,]



admin.site.register(Producer, ProducerAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceAccessories,AccessoriesAdmin)

