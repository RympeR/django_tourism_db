from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.shortcuts import render

from .models import *
from .serializers import *
from django.core import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

import json
import requests

# Create your views here.

#MAIN PAGE
def index(request):
    pass

#REG PAGES
def registration(requset):
    pass

def logout(request):
    pass


#STAFF PAGES
def client(request, user_id):
    pass

def gid(request, user_id):
    pass

def manager(request, user_id):
    pass

def director(request, user_id):
    pass
 

#MANAGER
def recrut_driver(request):
    pass

def get_list(request):
    pass

def create_excursion(request):
    pass

def take_gid(request):
    pass


#DIRECTOR
def update_salary(request):
    pass

def remove_staff(request):
    pass


def get_staff_list(request):
    pass

def recruit_staff(request):
    pass

def update_excursion_price(request):
    pass

def add_service(request):
    pass

#GID
def create_way(request):
    pass

#CLIENT
def order_excursion(request):
    pass


class RecrutDriver(APIView):

    def put(self, request):
        pass

class InsertUser(APIView):

    def post(self, request):
        pass


class CreateWay(APIView):

    def post(self, request):
        pass


class UpdatePrice(APIView):

    def put(self, request):
        pass


class StaffAPI(APIView):

    def get(self, request):
        pass

    def post(self, request):
        pass


class CreateService(APIView):

    def post(self, request):
        return Response({'status': 'success'})


class ExcursionAPI(APIView):

    def get(self, request):
        pass

    def post(self, request):
        return HttpResponse('POST request!')
