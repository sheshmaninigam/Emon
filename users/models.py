from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from cars.models import AddCar

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, default='1')
    image = models.ImageField(default='profilepic.jpg', upload_to='profile_picture')
    location = models.CharField(max_length=100)
    user_type = models.CharField(max_length=200,default="user")

    def __str__(self):
        return self.user.username

class Address(models.Model):
    code = models.ForeignKey(AddCar, default=0, on_delete = models.CASCADE,)
    no = models.IntegerField(validators=[MinValueValidator(0)],default=0)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.IntegerField(validators=[MinValueValidator(100)])


    def __str__(self) :
        return self.name
    
    @property
    def addcar_id(self):
        return self.code.id if self.code else None
    

class transaction(models.Model):
    user = models.ForeignKey(User,max_length=200,on_delete= models.CASCADE)
    trans = models.CharField(max_length=100)
    order = models.IntegerField(validators=[MinValueValidator(0)]) 
    statuses = models.CharField(max_length=100)
    date_time = models.CharField(default=0,max_length=100)
    brand = models.CharField(default="abc",max_length=100)
    model = models.CharField(default="abc",max_length=100)
    price = models.IntegerField(default=0,validators=[MinValueValidator(0)])
    name = models.CharField(default="abc",max_length=100)
    email = models.EmailField(default="abc",max_length=100)
    address = models.CharField(default="abc",max_length=300)
    city = models.CharField(default="abc",max_length=100)
    state = models.CharField(default="abc",max_length=100)
    postal_code = models.IntegerField(default=0,validators=[MinValueValidator(100)])

    def __str__(self) :
        return  f"Date: {self.date_time} & Cars: {self.brand}"