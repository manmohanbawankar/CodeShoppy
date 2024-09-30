from django.contrib import admin

# Register your models here.
from .models import Contacts, Customer, Admin, Sell

admin.site.register(Contacts)
admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(Sell)