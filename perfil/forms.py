
from django.forms import ModelForm
from .models import AccountModel

class AccountForm(ModelForm):
    class Meta:
        model = AccountModel
        fields = ['business_name','telephone', 'country','state','postal_code']

