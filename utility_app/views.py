from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms.AuthForms import CustomerRegistrationForm, RepresentativeRegistrationForm, CustomLoginForm, StatusForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from utility_app.models import ServiceRequest
from .forms.ServiceForms import ServiceRequestStatusUpdateForm, ServiceRequestForm, ResolvedAtForm


def customer_registration(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'Customer/customer_registration.html', {'form': form})


def representative_registration(request):
    if request.method == 'POST':
        form = RepresentativeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RepresentativeRegistrationForm()
    return render(request, 'Representative/representative_registration.html', {'form': form})


def login_view(request):
    user = request.user
    if user.is_authenticated:
        # Redirect to another view based on user role or any other criteria
        if user.role == 'CU':
            return redirect('view_profile')
        elif user.role == 'RE':
            return redirect('representative_dashboard')
        
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to appropriate view based on user role
                if user.role == 'CU':
                    return redirect('view_profile')
                elif user.role == 'RE':
                    return redirect('representative_dashboard')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def user_profile(request):
    # Fetch the profile information of the logged-in user
    user_profile = request.user
    return render(request, 'Customer/user_profile.html', {'user_profile': user_profile})

@login_required
def re_profile(request):
    # Fetch the profile information of the logged-in user
    user_profile = request.user
    return render(request, 'Representative/dashboard.html', {'user_profile': user_profile})

# Service Request Views
@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user  # Associate request with current user
            service_request.save()
            success_message = "Service request created successfully!"
            return redirect('view_profile')
    else:
        form = ServiceRequestForm()
    return render(request, 'Service/create_service.html', {'form': form})

@login_required
def user_service_requests(request):
    # Fetch all service requests associated with the logged-in user
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'Service/user_service_requests.html', {'service_requests': service_requests})

@login_required
def service_request_details(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    return render(request, 'Service/service_request_details.html', {'service_request': service_request})


# Representative Views
@login_required
def all_service_requests(request):
    if request.user.role != 'RE':
        return HttpResponseForbidden("You don't have permission to access this page.")
    
    service_requests = ServiceRequest.objects.all()
    print(service_requests)
    return render(request, 'Representative/dashboard.html', {'service_requests': service_requests})

@login_required
def update_service_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)

    if request.method == 'POST':
        if request.user.role != 'RE':
            return HttpResponseForbidden("You don't have permission to update service requests.")
        
        form = ServiceRequestStatusUpdateForm(request.POST, instance=service_request)
        
        if form.is_valid():
            form.save()
            return redirect('representative_dashboard')

@login_required
def update_resolved_at(request, request_id):
    request_object = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        if request.user.role != 'RE':
            return HttpResponseForbidden("You don't have permission to update resolved at.")
        
        form = ResolvedAtForm(request.POST)
        if form.is_valid():
            request_object.resolved_at = form.cleaned_data['resolved_at']
            request_object.save()
            return redirect('representative_dashboard')
