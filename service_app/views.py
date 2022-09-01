from audioop import reverse
import json
import random
import requests
from django.shortcuts import redirect, render
from django.views.generic.base import View
from .models import *


class GenerateView(View):
    def get(sefl, request): 
        return render(request, "service_app/index.html")


class NotificationView(View):
    def get(self, request, pk):
        notification = Notification.objects.get(id=pk)
        context = {'notification': notification}
        return render(request, "service_app/notification.html", context)


class SendNotificationView(View):
    def post(self, request):
        status = random.randint(1, 5)
        notification = Notification.objects.create(title='Title for status №: {0}'.format(str(status)), 
                                                status=status, 
                                                message='Message about notification for status {0}'.format(str(status)),
                                                url='some url')

        data = {'title': notification.title, 
                'status': notification.status, 
                'date': notification.created_at,
                'message': notification.message,
                'url': notification.url}

        pk=notification.id

        try:
            requests.post('http://127.0.0.1:1818/receive/', data=json.dumps(data))
        except:
            print("Connetion error")
        
        return redirect('notification', pk=pk)
