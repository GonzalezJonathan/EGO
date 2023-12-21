from rest_framework import serializers
from .models import Auto

class AutoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Auto
    fields = ('id','anio','modelo','precio','tipo','caracteristica','descripcion')