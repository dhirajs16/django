# Simple JWT

**Lessons**

- project_00 : [YT_Link](https://www.youtube.com/watch?v=PUzgZrS_piQ&list=PLlameCF3cMEtfyO6H7WXUAqoIJO21bDNp&index=1) Simple Auth 

- project_01 : [YT_Link](https://www.youtube.com/watch?v=lo7lBD9ynVc) Simple JWT Auth

<hr>

## Setup for default token

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


<hr>

## **Creating tokens manually**

### Step 1: Install Simple JWT and add to installed apps

Install the Simple JWT package.
```bash
pip install djangorestframework-simplejwt
```

Add to `settings.py` file:

```python

INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
    ...
]

```

### Step 2: Setup Corsheaders to avoid cors-policy error

Installation

```bash
pip install django-cors-headers
```

Configuration of cors headers in `settings.py` file

- Add it to your installed apps:

```bash
INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]
```
- Add corsheader middleware just above common middleware

```python
MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]
```
- Add url of the frontend
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
```

### Step 3: Setup Custom User model

[Docs](https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#a-full-example)

Use email for authentication instead of username 

- For model
```python
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Custom User model
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "tc"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

```

- For model manager
```python
# Customer model manager
class UserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2 = None):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name = name,
            tc = tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, password=None):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            name = name,
            tc = tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
```


