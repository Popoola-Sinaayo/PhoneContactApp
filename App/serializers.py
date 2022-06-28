from wsgiref.validate import validator
from rest_framework.serializers import ModelSerializer
from .models import Phone
from rest_framework import serializers


class PhoneSerializer(ModelSerializer):
    firstname = serializers.CharField(validators=[])
    lastname = serializers.CharField(validators=[])
    number = serializers.CharField(validators=[])

    class Meta:
        model = Phone
        fields = ('id', 'number', 'firstname', 'lastname')
