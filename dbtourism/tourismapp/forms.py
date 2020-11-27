from django import forms
from .models import *

class ClientForm(forms.Form):
    conteact_details = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    full_name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    login = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    passw = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))

class StaffForm(forms.Form):
    full_name = forms.CharField(max_length=90, widget=forms.TextInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    dolzhnost = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    salary = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    passport_data = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    work_status = forms.CharField(max_length=24, widget=forms.TextInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    the_foremost_place_of_work = forms.ModelChoiceField(queryset=TranscendingWork.objects.all(), widget=forms.Select(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))

class ExcursionForm(forms.Form):
    price = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    start_of_route = forms.ModelChoiceField(queryset=Route.objects.all(), widget=forms.Select(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    number_of_seats = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))

class UpdateSalaryForm(forms.Form):
    new_salary = forms.IntegerField( widget=forms.NumberInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    staff = forms.ModelChoiceField(queryset=Staff.objects.all(),widget=forms.Select( attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))

class UpdateExcursionPrcie(forms.Form):
    new_price = forms.IntegerField( widget=forms.NumberInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    excursion = forms.ModelChoiceField(queryset=Excursion.objects.all(),widget=forms.Select( attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))

class AddSightForm(forms.Form):
    name_of_attraction = forms.CharField(max_length=160, widget=forms.TextInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    description_of_attraction = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))

class RecruitDriverForm(forms.Form):
    id_staff = forms.ModelChoiceField(queryset=Staff.objects.filter(dolzhnost='водитель').all(), widget=forms.Select(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    id_excursion = forms.ModelChoiceField(widget=forms.Select( attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}),queryset=Excursion.objects.all())

class CreateWayForm(forms.Form):
    route_name = forms.CharField(max_length=160, widget=forms.TextInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    location_on_the_route = forms.ModelChoiceField(widget=forms.Select( attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}),queryset=Attraction.objects.all())
    next_attraction =  forms.ModelChoiceField(widget=forms.Select(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}),queryset=Route.objects.all())
    transition_time_in_minutes = forms.IntegerField( widget=forms.NumberInput(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    transport_delivered_to_the_sights = forms.ModelChoiceField(widget=forms.Select(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}),queryset=TypesOfTransport.objects.all() )

class RemoveStaffForm(forms.Form):
    full_name = forms.ModelChoiceField(widget=forms.Select(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}),queryset=Staff.objects.all())

class GetListForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'required': False, 'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker1', 'style': 'width:30%;'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'required': False, 'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker2', 'style': 'width:30%;'}))

class OrderExcursion(forms.Form):
    id_excursion = forms.ModelChoiceField(queryset=Excursion.objects.all(), widget=forms.Select(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'required': False, 'class': 'form-control datetimepicker-input', 'data-target': '#datetimepicker1', 'style': 'width:30%;'}))

class OrderGid(forms.Form):
    id_staff = forms.ModelChoiceField(queryset=Staff.objects.filter(dolzhnost='гид').all(), widget=forms.Select(attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}))
    id_excursion = forms.ModelChoiceField(widget=forms.Select( attrs={'required': False, 'class': 'form-control', 'style': 'width:30%;'}),queryset=Excursion.objects.all())

