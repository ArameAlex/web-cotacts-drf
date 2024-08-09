from django.db import models

from django.contrib.auth import get_user_model

user = get_user_model()

class Contacts(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='contacts')
