from django.contrib import admin

# Register your models here.
# admin.py

from .models import Subject

admin.site.register(Subject)

from .models import Notice

admin.site.register(Notice)
