# GasTrackPro

This Django application offers customer service functionalities for a gas utility company.
It enables customers to submit service requests, monitor their status, and manage their account information. 
Furthermore, representatives can manage service requests and provide support to customers.

## Endpoints

### Authentication
- Register Customer: `/register/customer/`
  - Allows customers to register for an account.
  - Access: Navigate to the registration page and fill out the registration form.

- Register Representative: `/register/representative/`
  - Allows representatives to register for an account.
  - Access: Navigate to the registration page and fill out the registration form.

- Login: `/login/`
  - Allows users to log in to their accounts.
  - Access: Navigate to the login page and enter your credentials.

- Logout: `/logout/`
  - Allows logged-in users to log out of their accounts.
  - Access: Click on the logout button while logged in.

- User Profile: `/profile/`
  - Displays the profile information of the logged-in user.
  - Access: Requires user authentication.

### Service Requests
- Create Service Request: `/create/`
  - Allows customers to submit a new service request.
  - Access: Requires user authentication.

- User Service Requests: `/service-requests/`
  - Displays a list of service requests submitted by the logged-in customer.
  - Access: Requires user authentication.

- Service Request Details: `/service-requests/int:request_id/`
  - Displays detailed information about a specific service request.
  - Access: Requires user authentication.

### Representative Dashboard
- All Service Requests: `/all-service-requests/`
  - Displays a list of all service requests for representatives.
  - Access: Requires representative authentication.

- Update Service Request: `/update_service_request/int:request_id/`
  - Allows representatives to update the status of a service request.
  - Access: Requires representative authentication.

- Update Resolved At: `/update_resolved_at/int:request_id/`
  - Allows representatives to update the resolved date and time of a service request.
  - Access: Requires representative authentication.
