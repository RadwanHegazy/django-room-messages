from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save




class Room (models.Model) :
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User,related_name='users_room')

    def __str__(self) : 
        return f'{self.name}'



class Message (models.Model) : 
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User,related_name='sender_user',on_delete=models.CASCADE)
    
    def __str__(self) :
        return f'{self.sender} : {self.text} , to {self.room.name} at {self.date}'


