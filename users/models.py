from django.db import models
from django.core.validators import RegexValidator



phone_validator = RegexValidator(
    regex=r'^\d{10}$',
    message="Enter a valid 10 digit mobile number"
)


    
class UserRegister(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10, validators=[phone_validator])
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email
    
class package(models.Model):

    fort_name = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    pickup_place = models.CharField(max_length=150)
    pickup_date = models.DateField()
    seats = models.IntegerField()
    price = models.IntegerField()
    offer_price = models.IntegerField()

    created_by_user = models.BooleanField(default=False)

    def seats_left(self):
     return self.seats
    
from django.db import models

class Booking(models.Model):
    package = models.ForeignKey(package, on_delete=models.CASCADE)
    
    
    booking_id = models.AutoField(primary_key=True)
    your_name = models.CharField(max_length=100)
    your_address = models.TextField()
    your_contact = models.CharField(max_length=15)
    your_email = models.EmailField(max_length=100)
    driver_name = models.CharField(max_length=100)
    trip_date = models.DateField()
    contact = models.CharField(max_length=15)
    package_name = models.CharField(max_length=100)
    seats_booked = models.IntegerField(default=1)
    total_price = models.IntegerField(default=0)  # default ठेवा
    payment_method = models.CharField(max_length=20, default="Cash")

    def __str__(self):
        return self.your_name
    
    
class LoginHistory(models.Model):
    user = models.ForeignKey(UserRegister, on_delete=models.CASCADE)
    email = models.EmailField()
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    
