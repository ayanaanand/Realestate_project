# listings/admin.py

from django.contrib import admin
from .models import Property


# Register the Property model
admin.site.register(Property)

from django.contrib import admin
from .models import ContactMessage

# Admin class to customize how the ContactMessage model is displayed in the admin interface
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')  # Fields to display in the list view
    search_fields = ('name', 'email')  # Fields to search by in the admin
    list_filter = ('submitted_at',)  # Filter options by submission date
    ordering = ('-submitted_at',)  # Order by the most recent submissions first

# Register the ContactMessage model with the admin site
admin.site.register(ContactMessage, ContactMessageAdmin)
