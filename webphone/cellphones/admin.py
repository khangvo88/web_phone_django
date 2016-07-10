from django.contrib import admin

# Register your models here.
from .models import Producer, Smartphone



#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Smartphone
    extra = 2
    

class ProducerAdmin(admin.ModelAdmin):
            
    fieldsets = [
        (None       ,{'fields':['name']}),
        ('Date info',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('name','pub_date','was_startup_company')
    list_filter =['pub_date']
    search_fields = ['name']
    date_hierarchy ='pub_date'
    #list_per_page = 100 #default
    
    # ?????????
    #list_select_related = ('name','pub_date') #LEARN LATER    

class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ('phone_model','price','producer')            

admin.site.register(Producer, ProducerAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)

