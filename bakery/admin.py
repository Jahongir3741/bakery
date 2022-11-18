from django.contrib import admin
from .models import Bakery, Bread, BreadItem

admin.site.register([Bakery, Bread, BreadItem])
