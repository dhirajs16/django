from channels.consumer import AsyncConsumer, SyncConsumer

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Websocket connect.....', event)
    
    async def websocket_disconnect(self, event):
        print('Websocket disconnect....', event)
    
    async def websocket_receive(self, event):
        print('Websocket received......', event)
        
        
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Websocket connect.....', event)
    
    def websocket_disconnect(self, event):
        print('Websocket disconnect....', event)
    
    def websocket_receive(self, event):
        print('Websocket received......', event)
      