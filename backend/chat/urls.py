from django.urls import path
from .views import *

urlpatterns = [
    path('messages', MessageAPIView.as_view())
]