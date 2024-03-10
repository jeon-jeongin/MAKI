from django.urls import path

from .views import AnimationList

urlpatterns = [
    path(route='animations', view=AnimationList.as_view(), name="animation_list")
]
