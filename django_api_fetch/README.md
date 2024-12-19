# Requests Library for Data Fetching

## Step 1: Install the Requests Library

If you haven't already installed the `requests` library, you can do so using pip:

```bash
pip install requests
```

## Step 2: Create a Service Module

It's a good practice to keep API calls separate from your views. Create a new file named `services.py` in your app directory:

```python
# myapp/services.py
import requests

def fetch_data(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as error:
        # Handle any exceptions that occur during the request
        print(f"Request failed: {error}")
        return None
```

## Step 3: Use the Service in Your Views

Now, you can use this service function in your views to fetch data from the third-party API:

```python
# myapp/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import fetch_data

class ThirdPartyDataView(APIView):
    def get(self, request):
        url = "https://api.example.com/data"
        params = {"key": "value"}  # Optional parameters
        data = fetch_data(url, params)
        
        if data:
            return Response(data)
        else:
            return Response({"error": "Failed to fetch data"}, status=500)
```

## Step 4: Define URL Patterns

Add a URL pattern for your view in your app's `urls.py`:

```python
# myapp/urls.py
from django.urls import path
from .views import ThirdPartyDataView

urlpatterns = [
    path('third-party-data/', ThirdPartyDataView.as_view(), name='third_party_data'),
]
```

## Step 5: Include App URLs in Main Project

Make sure to include your app's URL patterns in your main project's `urls.py`:

```python
# project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),
]
```

## Step 6: Run the Server and Test

Run your Django server:

```bash
python manage.py runserver
```

You can now test your API endpoint using tools like Postman or cURL to fetch data from the third-party API.

### Example Use Case

Suppose you want to fetch a list of popular Python repositories from GitHub's API:

```python
# app/services.py
def fetch_github_repos():
    url = "https://api.github.com/search/repositories"
    params = {"q": "language:python", "sort": "stars", "order": "desc"}
    return fetch_data_from_third_party_api(url, params)
```

Then, modify your view to use this function:

```python
# app/views.py
class GitHubReposView(APIView):
    def get(self, request):
        data = fetch_github_repos()
        return Response(data)
```

Add a URL pattern for this view:

```python
# app/urls.py
path('github-repos/', GitHubReposView.as_view(), name='github_repos'),
```
