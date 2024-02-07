from .models import *
from rest_framework import serializers

class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model=PRODUCTION
        fields='__all__'
        
        
class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producer
        fields='__all__'
        
        
        
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'