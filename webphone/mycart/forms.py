from django.forms import CharField, EmailField, PasswordInput
from django.forms import Form, ModelForm
from django.contrib.auth.models import User


# class MyUserForm(Form):
#     username = CharField(label='username', max_length=100)
#     firstname = CharField(label='first_name', max_length=100)
#     lastname  = CharField(label='last_name', max_length=100)
#
#     email = EmailField(label='email', max_length=100, required=False)
#
#     password = CharField(widget=PasswordInput())


class MyUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name','last_name']

class LoginForm(Form):
    username = CharField(label='username', max_length=100)
    password = CharField(widget=PasswordInput())