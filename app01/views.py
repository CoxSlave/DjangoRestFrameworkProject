from django.shortcuts import render




from rest_framework.views import APIView
from rest_framework.response import Response

class home(APIView):

    def get(self,request):

        return Response("我是 DRF GET")

    def post(self, request):

        return Response("我是 DRF POST")