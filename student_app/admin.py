from django.contrib import admin

# Register your models here.
# admin.py

from .models import Subject

admin.site.register(Subject)

from .models import Notice

admin.site.register(Notice)

# for contact page submission
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')