from django import forms
from cars.models import AddCar,Contacts

class AddCars_Forms(forms.ModelForm):
    class Meta:
        model = AddCar
        fields=["cars_code","cars_person_name","cars_name","cars_model","cars_price","cars_desc","cars_image"]

class Contact_Forms(forms.ModelForm):
    class Meta:
        model = Contacts
        fields=["first_name","last_name","email","phone","messages"]