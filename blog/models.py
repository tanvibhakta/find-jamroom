from django.db import models
from django.utils import timezone

#ForeignKey, ManyToManyField, OneToOneField

class Owner(models.Model):
    """docstring for Owner."""
    owner_name = models.CharField(max_length=100)
    owner_ph_no = models.CharField(max_length=12)

    def __str__(self):
        return self.owner_name

class Jamroom(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.TextField()
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    owner_id = models.ForeignKey(Owner)
    # operating_hours = models.ForeignKey(OperatingHours)

    def __str__(self):
        return self.name

class OperatingHours(models.Model):
    """docstring for Operating_hours."""
    jamroom_id = models.ForeignKey(Jamroom)
    # 0 = Sunday, 6 = Saturday
    weekday = models.IntegerField()
    start_hour = models.TimeField(auto_now=False, auto_now_add=False)
    end_hour = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.jamroom_id

class Customer(models.Model):
    """docstring for Customer."""
    customer_name = models.CharField(max_length=100)
    booking_istrue = models.BooleanField()

    def __str__(self):
        return self.customer_name

class Booking(models.Model):
    """docstring for Booking."""
    customer_id = models.ForeignKey(Customer)
    jamroom_id = models.ForeignKey(Jamroom)
    booked_time_slot = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.customer_id

"""
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    """
