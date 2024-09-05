from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework import status
from .geturl import get_url
from .models import QuizModel
from .posturl import send_quizzes_to_server
from django.http import HttpResponse, JsonResponse

class GetDBClone(APIView):
    def get(self, request, format=None):
        return Response(get_url())
    
    def post(self, request, format=None):
        success = send_quizzes_to_server()
        if success:
            return Response({"detail": "Quizzes successfully sent to server!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "Error occurred while sending quizzes."}, status=status.HTTP_400_BAD_REQUEST)
    


    
