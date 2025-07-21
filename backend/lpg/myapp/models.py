from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Cascade - deletes a record permanently
    mobile_no = models.CharField(max_length=10)
    consumer_no = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username

class Booking(models.Model):
    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('out-for-delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]

    name = models.CharField(max_length=100)
    consumer_number = models.CharField(max_length=20)
    delivery_date = models.DateField()
    time_slot = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='booked')

    def __str__(self):
        return f"Booking by {self.name} on {self.delivery_date} during {self.time_slot}"


class Employee(models.Model):
    employeeid = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=10)

    def __str__(self):
        return self.employeeid