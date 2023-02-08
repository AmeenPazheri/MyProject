from django.contrib import admin

# Register your models here.
from .models import Place,executives
admin.site.register(Place)
admin.site.register(executives)