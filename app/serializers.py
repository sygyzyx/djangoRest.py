from dataclasses import field
from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        field = ('id', 'Name', 'Address') 
        #OR fields = '__all__'
