# **Django with All Auth**

[Installation](https://pypi.org/project/django-allauth/) | [Docs](https://docs.allauth.org/en/latest/) | [YouTube](https://www.youtube.com/watch?v=RtUMOPv6Lq0) 


To integrate GitHub authentication into a Django application using `django-allauth`, follow these detailed steps:

## Step 1: Set Up Your Django Project

1. **Create a Django Project**: If you haven't already, create a new Django project.
   ```bash
   django-admin startproject myproject
   cd myproject
   ```

2. **Create an App**: Create a new app within your project.
   ```bash
   python manage.py startapp myapp
   ```

3. **Install django-allauth**: Install `django-allauth` using pip.
   ```bash
   pip install django-allauth
   ```

   For social account functionality, including providers like Google, Facebook, and Twitter, you can also install the necessary dependencies by using:
    ```bash
    pip install "django-allauth[socialaccount]"
    ```
4. **Add to Installed Apps**: Update your `settings.py` to include the necessary apps.
   ```python
   INSTALLED_APPS = [
       ....

       'django.contrib.sites',  # Required for allauth
       'allauth',               # Main allauth app
       'allauth.account',       # Account management
       'allauth.socialaccount', # Social account management
       'allauth.socialaccount.providers.github',  # GitHub provider

        'allauth.socialaccount.providers.google',     # Google provider
        'allauth.socialaccount.providers.facebook',   # Facebook provider
        'allauth.socialaccount.providers.twitter',     # Twitter (X) provider
   ]
   ```

5. **Set the Site ID**: Add the following line to your `settings.py`:
   ```python
   SITE_ID = 1  # Default site ID, ensure this matches your site in the admin panel
   ```

## Step 2: Configure Authentication Backends

In `settings.py`, specify the authentication backends:
```python
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",  # Default backend
    "allauth.account.auth_backends.AuthenticationBackend",  # Allauth backend
)
```

## Step 3: Set Up URLs

1. **Update `urls.py`**: Include the allauth URLs in the project's  `urls.py` file.
   ```python
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('accounts/', include('allauth.urls')),  # Allauth URLs for account management
       ...
   ]
   ```


## Step 4: Configure GitHub Provider in Settings

Add the following configuration to your `settings.py`:
```python
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'APP': {
            'client_id': GITHUB_CLIENT_ID,
            'secret': GITHUB_CLIENT_SECRET,
            'key': ''
        }
    }
}
```
NOTE: initialize IDs' and SECRET KEYS in the `.env` file.

## Step 5: Run Migrations

Run the necessary migrations for `django-allauth`:
```bash
python manage.py migrate
```

## Step 6: Create a GitHub OAuth Application

1. **Login to GitHub**: Go to your GitHub account settings and navigate to Developer settings > OAuth Apps.

2. **Register a New Application**:
   - Click on "New OAuth App".
   - Fill in the application details:
     - **Homepage URL**: Your site's URL (e.g., `http://127.0.0.1:8000/`).
     - **Authorization callback URL**: This should be `http://127.0.0.1:8000/accounts/github/login/callback/`.
