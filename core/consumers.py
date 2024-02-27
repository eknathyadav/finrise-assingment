from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import User
from asgiref.sync import sync_to_async


class LiveFeedConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].is_anonymous:
            # Reject the connection
            # await self.send(text_data=json.dumps({
            #     'message': "You are not authorized to subscribe to live feed"
            # }))
            self.group_name = None
            await self.close()
        else:

            self.group_name = 'binance_live_feed'

            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name
            )

            await self.accept()

    async def feed_message(self, event):

        await self.send(text_data=json.dumps(
            {
                'message': event["message"]
            }
        ))

    async def disconnect(self, code):

        # if self.group_name:
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
