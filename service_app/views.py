from audioop import reverse
import json
import random
from datetime import date, datetime

import requests
from django.shortcuts import redirect, render
from django.views.generic.base import View
from .models import *
from icecream import ic

class GenerateView(View):
    def get(self, request):
        return render(request, "service_app/index.html")


class SendNotificationView(View):
    def post(self, request):

        data_1 = {'title': 'Дела с проектом!!',
                'status': 'Выполнить в ближайшее время',
                'created_at': str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                'message': [
                            {"key": "ucl-1", "summary": "описание тикета1","date":"дата внутри сообщения!!!"},
                            {"key": "ucl-2", "summary": "описание тикета1"},
                            {"key": "ucl-3", "summary": "описание тикета1"}
                        ],
                'url': 'https://www.lipsum.com/',
                'notification_group': 2,
                'recipient': ["razzakov334@gmail.com", "99169335"]}

        data_2 = {
            'title': 'Дела с проектом!!',
            'status': 'Выполнить в ближайщее время',
            'created_at': str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            'message': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                    "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
                    "when an unknown printer took a galley of type and scrambled it to make a type "
                    "specimen book. It has survived not only five centuries, but also the leap into electronic "
                    "typesetting, remaining essentially unchanged. It was popularised in the 1960s with the "
                    "release of Letraset sheets containing Lorem Ipsum passages, and more recently "
                    "with desktop publishing software like Aldus PageMaker including versions of "
                    "Lorem Ipsum.",
            'url': 'https://www.lipsum.com/',
            'notification_group': 3,
            'recipient': ["razzakov334@gmail.com", "99169335"]
        }

        data_3 = {
            'title': 'Вы просрочили проект!!',
            'status': 'Критический',
            'created_at': str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            'message': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
                    "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
                    "when an unknown printer took a galley of type and scrambled it to make a type "
                    "specimen book. It has survived not only five centuries, but also the leap into electronic "
                    "typesetting, remaining essentially unchanged. It was popularised in the 1960s with the "
                    "release of Letraset sheets containing Lorem Ipsum passages, and more recently "
                    "with desktop publishing software like Aldus PageMaker including versions of "
                    "Lorem Ipsum.",
            'url': 'https://www.lipsum.com/',
            'notification_group': 3,
            'recipient': ["razzakov334@gmail.com", "99169335"]
        }

        data_4 = {
            'title': 'Дела с проектом!!',
            'status': 'Выполнить в ближайшее время',
            'created_at': str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            'message': [{"summary":"Ты завтра дежуришь"}],
            'url': 'https://www.lipsum.com/',
            'notification_group': 1,
            "recipient": ["razzakov334@gmail.com", "99169335"]
        }

        data_list = [data_1, data_2, data_3, data_4]
        random_index = random.randint(0, len(data_list) - 1)

        final_data = (data_list[random_index])
        print(final_data)
                                               
        try:
            requests.post('http://127.0.0.1:8022/receive/', data=json.dumps(final_data))
            print('connection')
        except:
            print("Connetion error")

        return render(request, "service_app/notification.html", {'data': final_data})
