"""
from rest_framework import serializers
from .models import Recieve

class RecieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recieve
        fields = ('name', 'device')
        """