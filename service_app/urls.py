from django.urls import path
from .views import *

urlpatterns = [
    path('', GenerateView.as_view()),
    path('generate/', SendNotificationView.as_view(), name='generate'),
]
