# Simple JWT

**Lessons**

- project_00 : [YT_Link](https://www.youtube.com/watch?v=PUzgZrS_piQ&list=PLlameCF3cMEtfyO6H7WXUAqoIJO21bDNp&index=1) Simple Auth 

- project_01 : [YT_Link](https://www.youtube.com/watch?v=lo7lBD9ynVc) Simple JWT Auth

<hr>

## Setup 

### Step 1: Install Django Rest Framework and Simple JWT

First, ensure you have Django and Django Rest Framework installed. If not, you can install them using pip:

```bash
pip install django
pip install djangorestframework
```

Next, install the Simple JWT package:

```bash
pip install djangorestframework-simplejwt
```

### Step 2: Configure Django Project

1. **Create a Django Project**: If you haven't already, create a new Django project:

   ```bash
   django-admin startproject project_name
   ```

2. **Create a Django App**: Navigate into your project directory and create a new app:

   ```bash
   python manage.py startapp app_name
   ```

3. **Add Apps to `INSTALLED_APPS`**: In your project's `settings.py`, add `'rest_framework'` and `'rest_framework_simplejwt'` to `INSTALLED_APPS`:

   ```python
   INSTALLED_APPS = [
       # ...
       'rest_framework',
       'rest_framework_simplejwt',
       # ...
   ]
   ```

### Step 3: Configure JWT Authentication

In your `settings.py`, configure JWT authentication settings:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    # Other settings as needed
}
```

### Step 4: Define JWT Token Endpoints

In your app's `urls.py`, define routes for JWT token generation and refresh:

```python
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

### Step 5: Implement User Authentication

1. **Create User Model**: Use Django's built-in `User` model or create a custom user model by extending `AbstractUser`.

2. **Implement Login and Registration Views**: Create views for user login and registration. Use `TokenObtainPairView` for login, which returns an access and refresh token pair.

## Step 6: Protect API Endpoints

Use the `IsAuthenticated` permission class to protect API endpoints that require authentication:

```python
from rest_framework.permissions import IsAuthenticated

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Only authenticated users can access this view
        return Response({"message": "Hello, authenticated user!"})
```

### Step 7: Test JWT Authentication

1. **Run the Server**: Start your Django server:

   ```bash
   python manage.py runserver
   ```

2. **Test JWT Tokens**: Use tools like Postman or cURL to test token generation and protected endpoint access.
