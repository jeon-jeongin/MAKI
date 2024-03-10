from rest_framework import generics
from .models import Animation
from .serializers import AnimationSerializer

class AnimationList(generics.ListAPIView):
  serializer_class = AnimationSerializer
  model = Animation
  queryset = Animation.objects.all()