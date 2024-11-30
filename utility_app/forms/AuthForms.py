from django import forms
from django.contrib.auth.forms import UserCreationForm
from utility_app.models import CustomUser, ServiceRequest
from django.contrib.auth.forms import AuthenticationForm

class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super(CustomerRegistrationForm, self).save(commit=False)
        user.role = CustomUser.CUSTOMER
        if commit:
            user.save()
        return user

class RepresentativeRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super(RepresentativeRegistrationForm, self).save(commit=False)
        user.role = CustomUser.REPRESENTATIVE
        if commit:
            user.save()
        return user

class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class StatusForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status']
