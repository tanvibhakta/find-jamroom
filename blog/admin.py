from django.contrib import admin
# from django.db.models import get_models, get_app
from .models import Owner, Jamroom, OperatingHours, Customer, Booking

admin.site.register(Owner)
admin.site.register(Jamroom)
admin.site.register(OperatingHours)
admin.site.register(Customer)
admin.site.register(Booking)
