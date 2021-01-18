# todo/views.py
from django.shortcuts import render
from requests.models import Response
from rest_framework import viewsets          # add this
import requests
from .serializers import TodoSerializer      # add this
from .models import Todo                     # add this


class TodoView(viewsets.ModelViewSet):       # add this
    serializer_class = TodoSerializer          # add this
    queryset = Todo.objects.all()              # add this

    def list(self, request):
        api_data_res = requests.get("https://evilinsult.com/generate_insult.php?lang=es&type=json")
        output_data = api_data_res.json()
        test_queryset = Todo.objects.all()
        serializer = TodoSerializer(test_queryset,many=True)
        return Response({'something': 'my custom JSON'})
