from rest_framework import serializers
from .models import Animation, Image

class AnimationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Animation
    fields = '__all__'
    