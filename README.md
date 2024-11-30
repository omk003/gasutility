# Gas Utility

This Django application offers customer service functionalities for a gas utility company.
It enables customers to submit service requests, monitor their status, and manage their account information. 

1. Login  ![WhatsApp Image 2024-11-30 at 22 14 08_9624bb35](https://github.com/user-attachments/assets/d10c7982-2a4d-4d2a-ba25-532a1e29879f)
2. User profile ![WhatsApp Image 2024-11-30 at 22 15 15_0c9c4b24](https://github.com/user-attachments/assets/3d59bbc5-744e-4347-876b-fac69d632c90)
3. Creating service request ![WhatsApp Image 2024-11-30 at 22 15 50_d5a73ae6](https://github.com/user-attachments/assets/ca3e0270-ea82-4e33-92d8-a9ccf7028af9)
4. User view ![WhatsApp Image 2024-11-30 at 22 15 30_2ed6704b](https://github.com/user-attachments/assets/fdebdfc3-6870-4341-a768-69be45e30518)
5. Representative view ![WhatsApp Image 2024-11-30 at 22 13 48_4c60dffe](https://github.com/user-attachments/assets/dcac9c52-f4d5-45e1-9a4a-875b57719b4d)





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
