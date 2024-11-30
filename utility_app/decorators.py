from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group
from .models import CustomUser, ServiceRequest

content_type = ContentType.objects.get_for_model(ServiceRequest)

permission_customer, _ = Permission.objects.get_or_create(
    codename='can_access_service_requests_customer',
    name='Can Access Service Requests (Customer)',
    content_type=content_type,
)

permission_representative, _ = Permission.objects.get_or_create(
    codename='can_access_service_requests_representative',
    name='Can Access Service Requests (Representative)',
    content_type=content_type,
)

def assign_permissions_to_roles():
    
    customers = CustomUser.objects.filter(role='CU')
    for customer in customers:
        customer.user_permissions.add(permission_customer)

  
    representatives = CustomUser.objects.filter(role='RE')
    for representative in representatives:
        representative.user_permissions.add(permission_representative)

