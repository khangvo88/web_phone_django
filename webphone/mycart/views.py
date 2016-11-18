from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


from .forms import MyUserForm, LoginForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# message framework
from django.contrib import messages
from django.contrib.messages import get_messages

from django.views import generic
from .models import *


# Create your views here.

@login_required
#@permission_required('polls.can_vote')
def index(request):
    storage = get_messages(request)
    message_str = ""
    for message in storage:
        message_str = message_str + message.message
    return HttpResponse("<span>%s.</span><br/> Hello, You are in cart index."%message_str)
# def index(request):
#     return render(request, 'mycart/index.html')

@login_required
class IndexCartPage(generic.ListView):
    template_name = 'mycart/index.html'
    model = OrderItem
    context_object_name = 'items'
#    user = request.user

    def get_queryset(self):
        if self.request.session.get('cart_id', False):
            return OrderItem.objects.none()
            # cart = Order.objects.create(user=self.request["user"])
            # self.request.session['cart_id'] = cart.pk
        return OrderItem.objects.filter(cart=self.request.session['cart_id'])
        #return Device.objects.filter(status=STATUS_ACTIVE)


@login_required
class IndexOrderPage(generic.ListView):
    pass


@login_required
def create_user(request):
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save() # FIXME: should try/catch exception to check if saved successfully
            g = Group.objects.get(name='Registered')
            g.user_set.add(user)
            messages.add_message(request, messages.INFO, 'Add user successfully.')
            #messages.success(request, "Your data has been saved!")
            return HttpResponseRedirect(reverse('cart:index'))

    else:
        form = MyUserForm()
    return render(request, 'mycart/create_user.html', {'form':form})


def login_page(request):
    if request.user.is_authenticated():
        messages.add_message(request, messages.INFO,"You logged as <i>%s</i> already" %request.user.username)
        return HttpResponseRedirect(reverse('cart:index'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    messages.add_message(request, messages.INFO, "You has logged as %s" %user.username)
                    return HttpResponseRedirect(reverse('cart:index'))
                else:
                    messages.add_message(request, messages.INFO, "Your account had been deactivated by admin")
            else:
                messages.add_message(request, messages.INFO, "No account has been found")
            return render(request, 'mycart/login.html', {"form": form})
    else:
        form = LoginForm()
    return render(request, 'mycart/login.html',{"form":form})