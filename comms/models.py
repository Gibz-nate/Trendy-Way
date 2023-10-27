from django.db import models
from item.models import Item
from django.contrib.auth.models import User
# Create your models here.
class Communication(models.Model):
    item = models.ForeignKey(Item, related_name = 'comms', on_delete=models.CASCADE )
    members = models.ManyToManyField(User, related_name='comms')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('-modified_at',)


class CommunicationMessage(models.Model):
    communication = models.ForeignKey(Communication, related_name ='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)

    

