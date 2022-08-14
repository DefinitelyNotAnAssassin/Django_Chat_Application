from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class UserAccount(AbstractUser):
    unique_id = models.UUIDField(verbose_name="unique id")
    REQUIRED_FIELDS = ['unique_id']

    def __str__(self):
        return f'{self.username} | {self.unique_id}'

class Room(models.Model):
    room_name = models.CharField(max_length=32)
    room_id = models.UUIDField()
    participants = models.ManyToManyField(UserAccount, related_name = "rooms")

    def __str__(self):
        return f"{self.room_name} | {self.room_id}"
class Message(models.Model):
    sender = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    receiver = models.ManyToManyField(Room)
    content = models.CharField(max_length=255)
    message_id = models.UUIDField()
    def __str__(self):
        return f"{self.content} | {self.sender} | {self.message_id}"

