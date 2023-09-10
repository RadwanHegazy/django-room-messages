import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import Room, Message

class ChatConsumerForRooms(AsyncWebsocketConsumer):
    async def connect(self):
        
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'room_{self.room_name}'

        self.user = self.scope['user']

        self.room_model = Room.objects.get(name=self.room_name)



        # Join the group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)


        await self.accept()

    async def disconnect(self, close_code):


        await self.channel_layer.group_discard(
            self.room_group_name,self.channel_name
        )


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]


        if self.user in self.room_model.users.all() :
            Message.objects.create(
                room = self.room_model,
                text = message,
                sender = self.user,
            ).save()



        await self.channel_layer.group_send(
            self.room_group_name,{'type':'chat.message',"message":f"{self.user.username} : {message}"}
        )


    async def chat_message (self, event) :
        message = event['message']

        # print(event)

        await self.send(text_data=json.dumps({"message":message}))
        

