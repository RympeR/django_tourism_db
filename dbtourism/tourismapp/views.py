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
    context = {

    } 
    return render(request, 'tourism/index.html', context=context)

#REG PAGES
def registration(requset):
    context = {

    } 
    return render(request, 'tourism/registration.html', context=context)

def logout(request):
    context = {

    } 
    return render(request, 'tourism/logout.html', context=context)


#STAFF PAGES
def client(request, user_id):
    context = {

    } 
    return render(request, 'tourism/client.html', context=context)

def gid(request, user_id):
    context = {

    } 
    return render(request, 'tourism/gid.html', context=context)

def manager(request, user_id):
    context = {

    } 
    return render(request, 'tourism/manager.html', context=context)

def director(request, user_id):
    context = {

    } 
    return render(request, 'tourism/director.html', context=context)
 

#MANAGER
def recrut_driver(request):
    context = {

    } 
    return render(request, 'tourism/recrut_driver.html', context=context)

def get_list(request):
    context = {

    } 
    return render(request, 'tourism/get_list.html', context=context)

def create_excursion(request):
    context = {

    } 
    return render(request, 'tourism/create_excursion.html', context=context)

def take_gid(request):
    context = {

    } 
    return render(request, 'tourism/take_gid.html', context=context)


#DIRECTOR
def update_salary(request):
    context = {

    } 
    return render(request, 'tourism/update_salary.html', context=context)

def remove_staff(request):
    context = {

    } 
    return render(request, 'tourism/remove_staff.html', context=context)


def get_staff_list(request):
    context = {

    } 
    return render(request, 'tourism/get_staff_list.html', context=context)

def recruit_staff(request):
    context = {

    } 
    return render(request, 'tourism/recruit_staff.html', context=context)

def update_excursion_price(request):
    context = {

    } 
    return render(request, 'tourism/update_excursion_price.html', context=context)

def add_service(request):
    context = {

    } 
    return render(request, 'tourism/add_service.html', context=context)

#GID
def create_way(request):
    context = {

    } 
    return render(request, 'tourism/create_way.html', context=context)

#CLIENT
def order_excursion(request):
    context = {

    } 
    return render(request, 'tourism/order_excursion.html', context=context)


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
