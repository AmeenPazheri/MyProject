from django.contrib import admin

from .models import department,course,Application
admin.site.register(department)
admin.site.register(course)
admin.site.register(Application)
