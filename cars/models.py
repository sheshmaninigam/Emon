from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class AddCar(models.Model):
    cars_code = models.IntegerField(default=100,validators=[MinValueValidator(100)])
    cars_person_name = models.CharField(default="ABC",max_length=100)
    cars_name = models.CharField(max_length=100)
    cars_model = models.CharField(max_length=100)
    cars_price = models.IntegerField(validators=[MinValueValidator(0)])
    cars_desc = models.TextField()
    cars_image = models.ImageField(default='cars_image.jpg', upload_to='cars_image')

    def __str__(self):
        return self.cars_person_name
    
class Contacts(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(validators=[MinValueValidator(1111111111)])
    messages = models.TextField()

    def __str__(self):
        return self.first_name
