from django.db import models
from django.core.validators import RegexValidator

class UserRegister(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name
    
    
phone_validator = RegexValidator(
    regex=r'^\d{10}$',
    message="Enter a valid 10 digit mobile number"
)

class package(models.Model):                             #packages models
    fort_name = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10, validators=[phone_validator])
    pickup_place = models.CharField(max_length=150, default="Pune")
    pickup_date = models.DateField()
    seats = models.IntegerField()
    price = models.IntegerField()
    offer_price = models.IntegerField()
    
    def __str__(self):
        return self.fort_name