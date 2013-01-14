from django.forms import ModelForm, TextInput, PasswordInput
from django.contrib.auth.models import User
from models import *

class SellerForm(ModelForm):
    class Meta:
        model = Seller
        exclude = ('lat', 'lng', 'user')
        widgets = {
            'subtitle': TextInput(attrs={'placeholder': 'i.e. Violin Maker in Bath, UK'}),
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
        widgets = {
            'password': PasswordInput()
        }

class SellerContactForm(ModelForm):
    class Meta:
        model = SellerContact
        exclude = ('seller')
