from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from users.models import Profile,Address,transaction


class SignUpForms(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ["username", "email","first_name","last_name","password1","password2"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image","location"]

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["code","no","name","address","city","state","postal_code"]

class TranscationForm(forms.ModelForm):
    class Meta:
        model = transaction
        fields = ["user","trans","order","statuses","date_time","brand","model","email","price","name","address","city","state","postal_code"]