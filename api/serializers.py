from rest_framework import serializers
from base.models import Contacts

from django.contrib.auth import get_user_model

user = get_user_model()

class Contacts_serializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'

class User_serializer(serializers.ModelSerializer):
    contacts = Contacts_serializer(read_only=True, many=True)

    class Meta:
        model = user
        fields = '__all__'
