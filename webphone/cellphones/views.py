#  ====== FOR TEMPLATES and VIEWS =======
#from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext

from django.contrib import messages
from .forms import NameForm, ContactForm, DeviceImageUploadForm

#  ====== MODELS =======
from .models import *
from django.db.models import Count, Case, When, Q
#from django.db.models import Sum, IntegerField

#  ====== UTILITTIZED FUNCTIONS  =======
from django.utils import timezone
from .helpers import handle_uploaded_file, cut_to_block_n

# Create your views here.
# class IndexView(generic.ListView):
#     #by default : <model name>_list.html
#     template_name = 'cellphones/index.djhtml'
#     context_object_name = "Device_list"
#
#     def get_queryset(self):
#         """Return the last five Device, only show availabe phone"""
#         return Device.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class IndexView(generic.ListView):
    template_name = 'cellphones/index.html'    
    context_object_name = "featured_products"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        categories = Device.list_category()
        recent_product_list = {}
        for k,v in categories.items():
            temp = Device.objects.filter(status=STATUS_ACTIVE,category=k).order_by('-updated_at')[:9]
            if temp:
                recent_product_list[v] = temp
        context['recent_product_list'] = recent_product_list

        recent_date = timezone.now() - datetime.timedelta(days=30)
        recommended_products = Device.objects.filter(
            Q(status=STATUS_ACTIVE),
            Q(is_featured=True) | Q(pub_date__gt=recent_date)
        ).order_by('-updated_at')[:9]
        num_show = int(len(recommended_products) / 3)
        if num_show > 0:
            context['recommended_products'] = recommended_products[:3*num_show]
        else:
            context['recommended_products'] = recommended_products
        return context
    
    def get_queryset(self):
        # FIXME: change to random order
        return Device.objects.filter(is_featured=True, status=STATUS_ACTIVE).order_by('-updated_at')[:6]
        
    
class ListProductBy(generic.ListView):
    template_name = 'cellphones/list_product.html'
    context_object_name = "device_list"
    
    def get_queryset(self):
        temp = Device.objects.select_related('Device','tablet')
        return [t.Device or t.tablet or t for t in temp]

class ProductDetailView(generic.DetailView):
    model = Device
    #by default : <model name>_detail.html
    template_name = 'cellphones/product-detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)

        recent_date = timezone.now() - datetime.timedelta(days=30)
        recommended_products = Device.objects.filter(
            Q(status=STATUS_ACTIVE),
            Q(is_featured=True) | Q(pub_date__gt=recent_date)
        ).order_by('-updated_at')[:9]
        context['recommended_products'] = cut_to_block_n(recommended_products)

        # TODO: add related-product
        related_products = Device.objects.filter(status=STATUS_ACTIVE,
                                                producer=self.object.producer,
                                                condition = self.object.condition,
                                                category = self.object.category
        )
        context['related_products'] = cut_to_block_n(related_products)

        return context

    def get_queryset(self):
        """Excludes inactive Device"""
        return Device.objects.filter(status=STATUS_ACTIVE)
    
def get_name(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = NameForm(request.POST)
        # checked whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to new url
            return HttpResponseRedirect(reverse('cellphones:index'))
    else:
        form = NameForm()
        
    return render(request, 'cellphones/name.djhtml',{"form":form})        

def contact(request):
    from django.core.mail import send_mail
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = ContactForm(request.POST)
        # checked whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
        
            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)        
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
        
    return render(request, 'cellphones/contact.djhtml', {"form":form})
        

def buy(request, Device_id):
    selected_phone = get_object_or_404(Device, pk=Device_id)
    try:
        quantity = int(request.POST['quantity'])
    except (ValueError, KeyError):
        return render(request,'cellphones/detail.djhtml',
                      { "Device": selected_phone,
                        "error_message": "Wrong quantity"
                        })
    if quantity <= 0:
        return render(request,'cellphones/detail.djhtml',
                  { "Device": selected_phone,
                    "error_message": "Quantity must be positive integer"
                    })
                
    selected_phone.total_sales += quantity
    selected_phone.save()    
    return HttpResponseRedirect(reverse('cellphones:detail',args=(selected_phone.id,)))


def upload_file(request):
    if request.method == 'POST':
        form = DeviceImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['file'])
                messages.info(request, 'Uploaded file')
            except:
                import sys
                messages.error(request, '%s' %sys.exc_info())
            return HttpResponseRedirect(reverse('cellphones:upload'))
    else:
        form = DeviceImageUploadForm()
    return render(request,'cellphones/upload.html',{"form":form})


def page_not_found(request):
    return render(request,'cellphones/404.html', status=404, context_instance=RequestContext(request))

