from django import forms
from utility_app.models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'attached_files']

class ServiceRequestStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status']

class ResolvedAtForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['resolved_at']