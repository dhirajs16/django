# **Django Channels**

## **How to setup Django Channels?**

### 1. Install Django Channels
First, you need to install Django Channels. You can do this using pip:

```bash
pip install channels
```

### 2. Update Django Settings
Next, you need to update your Django settings to include Channels:

```python
# settings.py

INSTALLED_APPS = [
    'channels',
    # other installed apps
]

# Specify the ASGI application
ASGI_APPLICATION = 'your_project_name.asgi.application'
```

### 3. Create ASGI Configuration
Create an `asgi.py` file in your project’s root directory (if it doesn’t exist already):

```python
# myproject/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from yourapp.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
```

### 4. Define WebSocket Routing
Create a `routing.py` file in your app directory to define the WebSocket URL routing:

```python
# myapp/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),
]
```

### 5. Create Consumers
Consumers are responsible for handling WebSocket connections. Create a `consumers.py` file in your app directory:

```python
# myapp/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.send(text_data=json.dumps({
            'message': message
        }))
```

### 6. Update Django URLs
Make sure your main `urls.py` file routes to your ASGI application:

```python
# myproject/urls.py
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include your app routing
    path('ws/', include('yourapp.routing')),
]
```

### 7. Run the Server
Finally, run your Django development server to start using Channels:

```bash
python manage.py runserver
```
