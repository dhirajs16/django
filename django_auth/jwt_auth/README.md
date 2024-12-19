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
