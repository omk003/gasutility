from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    CUSTOMER = 'CU'
    REPRESENTATIVE = 'RE'
    USER_ROLES = [
        (CUSTOMER, 'Customer'),
        (REPRESENTATIVE, 'Representative'),
    ]
    role = models.CharField(max_length=2, choices=USER_ROLES, default=CUSTOMER)


class ServiceRequest(models.Model):
    
    REQUEST_TYPES = [
        ('gas_leak', 'Gas Leak'),
        ('meter_installation', 'Meter Installation'),
        ('meter_repair', 'Meter Repair'),
        ('account_update', 'Account Update'),
        ('billing_issue', 'Billing Issue'),
        ('maintenance', 'Maintenance'),
        ('other', 'Other'),
    ]

    
    REQUEST_STATUSES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    details = models.TextField()
    attached_files = models.FileField(upload_to='service_request_files/', blank=True, null=True)
    status = models.CharField(max_length=50, choices=REQUEST_STATUSES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Service Request #{self.id} - {self.request_type} ({self.status})"
