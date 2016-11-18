#from django.shortcuts import render
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Smartphone, Producer
from django.http.response import HttpResponseRedirect

# Create your views here.
def index(request):    
    #return HttpResponse("Hello, word. You're at the cellphones index")
    smartphone_list = Smartphone.objects.order_by('-pub_date')
    template = loader.get_template('cellphones/index.djhtml')
    context = {
            'smartphone_list': smartphone_list}    
    #short-cut    
    #return render(request,'cellphones/index.djhtml',context)
    return HttpResponse(template.render(context, request))

def detail(request, smartphone_id):
    
    #short-cut
    #phone = get_object_or_404(Smartphone,pk=smartphone_id)        
    try:
        phone = Smartphone.objects.get(pk=smartphone_id)
        #producer = Producer.objects.get(pk=phone.)
    except Smartphone.DoesNotExist:
        raise Http404("Phone does not exist")
    
    return render(request,'cellphones/detail.djhtml',
                  {'phone':phone})
    

def buy(request, smartphone_id):
    selected_phone = get_object_or_404(Smartphone, pk=smartphone_id)    
    quantity = request.POST['quantity']
    selected_phone.total_sales += int(quantity)
    selected_phone.save()
    
    return HttpResponseRedirect(reverse('cellphones:detail',args=(selected_phone.id,)))    