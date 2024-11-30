from django.contrib import admin
from .models import CustomUser, ServiceRequest


admin.site.register(CustomUser)
admin.site.register(ServiceRequest)