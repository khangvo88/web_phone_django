from django import forms
from django.core.mail import send_mail


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender  = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)    
    
    
class BuyForm(forms.Form):
    pass

class DeviceImageUploadForm(forms.Form):
    title = forms.CharField(max_length=50, initial="Hello")
    file = forms.ImageField()
