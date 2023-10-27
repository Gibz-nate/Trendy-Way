from django.contrib import admin

from .models import Communication, CommunicationMessage 
# Register your models here.

admin.site.register(Communication)
admin.site.register(CommunicationMessage)


