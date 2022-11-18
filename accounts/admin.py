from django.contrib import admin
from .models import UserAccount, Diroctor, Vendor, Baker, Client, Staff

admin.site.register([UserAccount, Diroctor, Vendor, Baker, Client, Staff])
