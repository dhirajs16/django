# **Django Channels**

## **How to setup Django Channels?**

### 1. Install Django Channels
First, you need to install Django Channels. You can do this using pip:

```bash
pip install channels
pip install daphne
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
ASGI_APPLICATION = 'myproject.asgi.application'
```

### 3. Create ASGI Configuration
Create an `asgi.py` file in your project’s root directory (if it doesn’t exist already):

```python
# myproject/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from myapp.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

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
    path('ws/', include('myapp.routing')),
]
```

### 7. Run the Server
Instead of using `python manage.py runserver`, use Daphne to run your ASGI application:

```bash
daphne -p 8000 myproject.asgi:application
```
<hr>

## **Consumer**

Consumers are similar to Django views in that they handle the logic for handling requests. However, while views handle HTTP requests, consumers handle WebSocket connections.

The main types of consumers you can use:

### 1. **WebsocketConsumer**
- **Usage**: For handling WebSocket connections.
- **Methods**:
  - **connect**: Called when a WebSocket connection is opened.
  - **disconnect**: Called when the connection is closed.
  - **receive**: Called when a message is received.

Example:
```python
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        self.send(text_data=json.dumps({'message': data['message']}))
```

### 2. **AsyncWebsocketConsumer**
- **Usage**: An asynchronous version of `WebsocketConsumer` for handling WebSocket connections.
- **Methods**: Same as `WebsocketConsumer`, but all methods are asynchronous.

Example:
```python
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.send(text_data=json.dumps({'message': data['message']}))
```

### 3. **SyncConsumer**
- **Usage**: For handling other types of connections synchronously, such as custom protocols or background tasks.
- **Methods**: Defined by you, based on what events you expect.

Example:
```python
from channels.consumer import SyncConsumer

class MySyncConsumer(SyncConsumer):
    def my_custom_event(self, event):
        print("Received event:", event)
```

### 4. **AsyncConsumer**
- **Usage**: An asynchronous version of `SyncConsumer` for handling other types of connections asynchronously.
- **Methods**: Defined by you, based on what events you expect.

Example:
```python
from channels.consumer import AsyncConsumer

class MyAsyncConsumer(AsyncConsumer):
    async def my_custom_event(self, event):
        print("Received event:", event)
```

### Key Points
- **WebsocketConsumer** and **AsyncWebsocketConsumer** are specialized for WebSocket connections.
- **SyncConsumer** and **AsyncConsumer** are more general-purpose and can be used for custom protocols or background tasks.
