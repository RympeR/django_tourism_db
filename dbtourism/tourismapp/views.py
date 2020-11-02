from django.http import Http404
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import *
from .models import *
from .serializers import *
from django.core import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

import json
import requests
from datetime import datetime
# Create your views here.

#MAIN PAGE
def index(request):
    context={}
    return render(request, 'tourism/index.html', context=context)

#REG PAGES
def registration(request):
    context = {
        "form": ClientForm
    } 
    return render(request, 'tourism/registration.html', context=context)

def login(request):
    if request.method == 'POST':
        pass
        # id_profile = Client.
    return render(request, 'tourism/login.html')

def logout(request):
    del request.sesion['username']
    redirect(index)

#STAFF PAGES
def client(request, user_id):
    client_data = Client.objects.get(pk=user_id)
    context = {
        'client': client_data
    } 
    return render(request, 'tourism/client.html', context=context)

def gid(request, user_id):
    gid = Staff.objects.get(pk=user_id)
    context = {
        'staff': gid
    } 
    return render(request, 'tourism/gid.html', context=context)

def manager(request, user_id):
    manager = Staff.objects.get(pk=user_id)
    context = {
        'staff': manager
    } 
    return render(request, 'tourism/manager.html', context=context)

def director(request, user_id):
    director = Staff.objects.get(pk=user_id)
    context = {
        'staff': director
    } 
    return render(request, 'tourism/director.html', context=context)
 

#MANAGER
def recrut_driver(request):
    context = {
        'form': RecruitDriverForm
    } 
    return render(request, 'tourism/recrut_driver.html', context=context)

def get_list(request):
    context = {
        # 'order_list': KlientRaspisanie.objects.filter(date__range=('09-12-2000', '09-12-2000'))
        'form': GetListForm 
    } 
    return render(request, 'tourism/get_list.html', context=context)

def create_excursion(request):
    context = {
        'form': ExcursionForm
    } 
    return render(request, 'tourism/create_excursion.html', context=context)

def take_gid(request):
    context = {
        'form': OrderGid
    } 
    return render(request, 'tourism/take_gid.html', context=context)


#DIRECTOR
def update_salary(request):
    context = {
        'form': UpdateSalaryForm
    } 
    return render(request, 'tourism/update_salary.html', context=context)

def remove_staff(request):
    context = {
        'form' :RemoveStaffForm
    } 
    return render(request, 'tourism/remove_staff.html', context=context)


def get_staff_list(request):
    context = {
        'staff': Staff.objects.values('dolzhnost').all()
    } 
    return render(request, 'tourism/get_staff_list.html', context=context)

def recruit_staff(request):
    context = {
        'form' :StaffForm
    } 
    return render(request, 'tourism/recruit_staff.html', context=context)

def update_excursion_price(request):
    context = {
        'form': AddSightForm
    } 
    return render(request, 'tourism/update_excursion_price.html', context=context)

def add_sight(request):
    context = {
        "form":AddSightForm
    } 
    return render(request, 'tourism/add_sight.html', context=context)

#GID
def create_way(request):
    context = {
        'form': CreateWayForm
    } 
    return render(request, 'tourism/create_way.html', context=context)

#CLIENT
def order_excursion(request):
    context = {
        'form': OrderExcursion
    }
    return render(request, 'tourism/order_excursion.html', context=context)


class RecrutDriver(APIView):

    def post(self, request):
        form = RecruitDriverForm(request.POST)
        if form.is_valid():
            staff_excursion = StaffExcursion(
                id_staff=form.cleaned_data['id_staff'],
                id_excursion=form.cleaned_data['id_excursion']
            )
            staff_excursion.save()
            return Response({'status': 'success'})
        return Response({'status': False})

class InsertUser(APIView):

    def post(self, request):
        form = ClientForm(request.POST)

        if form.is_valid():
            client = Client(
                contact_details=form.cleaned_data['contact_details'],
                full_name=form.cleaned_data['full_name'],
                date_of_registration=datetime.today().strftime('%Y-%m-%d')
            )
            client.save()
            return Response({'status': 'success'})
        return Response({'status': False})

class CreateWay(APIView):

    def post(self, request):
        form = CreateWayForm(request.POST)
        if form.is_valid():
            Route.objects.create(
                route_name=form.cleaned_data['route_name'],
                location_on_the_route=form.cleaned_data['location_on_the_route'],
                next_attraction=form.cleaned_data['next_attraction'].id_route,
                transition_time_in_minutes=form.cleaned_data['transition_time_in_minutes'],
                transport_delivered_to_the_sights=form.cleaned_data['transport_delivered_to_the_sights'].id_transport,
            ).save()
            return Response({'data': 'success'})
        return Response({'data': False})

class UpdatePrice(APIView):

    def post(self, request):
        form = AddSightForm(request.POST)

        if form.is_valid():
            Excursion.objects.filter(
                id_excursion=form.cleaned_data['excursion'].id_excursion
            ).update(
                price=form.cleaned_data['new_price']
            ).save()
            return Response({'status': 'success'})
        return Response({'status': False})


class StaffAPI(APIView):

    def get(self, request):
        staff_id = request.GET['staff_id']
        staff = Staff.objects.get(pk=staff_id)
        return Response({'data': staff})

    def post(self, request):
        form = StaffForm(request.POST)

        if form.is_valid():
            staff = Staff(
                full_name=form.cleaned_data['full_name'],
                dolzhnost=form.cleaned_data['dolzhnost'],
                salary=form.cleaned_data['salary'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                passport_data=form.cleaned_data['passport_data'],
                work_status=form.cleaned_data['work_status'],
                the_foremost_place_of_work=form.cleaned_data['the_foremost_place_of_work']
            )
            staff.save()
            return Response({'status': 'success'})
        return Response({'status': False})


class CreateSight(APIView):

    def post(self, request):
        form = AddSightForm(request.POST)

        if form.is_valid():
            attraction = Attraction(
                name_of_attraction=form.cleaned_data['name_of_attraction'],
                description_of_attraction=form.cleaned_data['description_of_attraction']
            )
            attraction.save()
            return Response({'status': 'success'})
        return Response({'status': False})

class ExcursionAPI(APIView):

    def get(self, request):
        excursion_id = request.GET['id_excursion']
        excursion = Excursion.objects.get(pk=excursion_id)
        return Response({'data': excursion})

    def post(self, request):
        form = ExcursionForm(request.POST)
        if form.is_valid():
            excursion = Excursion(
                price=form.cleaned_data['price'],
                start_of_route=form.cleaned_data['start_of_route'],
                number_of_seats=form.cleaned_data['number_of_seats']
            )
            excursion.save()
            return Response({'status': 'success'})
        return Response({'status': False})
