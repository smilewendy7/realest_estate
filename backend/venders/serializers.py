from rest_framework import serializers
from .models import Vender

class VenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vender
        ## all the fields in the model
        fields = '__all__'

