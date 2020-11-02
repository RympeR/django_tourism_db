from django import forms
from .models import *

class ClientForm(forms.Form):
    conteact_details = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'required': False, 'class': 'dws-input'}))
    full_name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'required': False, 'class': 'dws-input'}))

class StaffForm(forms.Form):
    full_name = forms.CharField(max_length=90, widget=forms.TextInput(attrs={'required': False, 'class': 'dws-input'}))
    dolzhnost = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'required': False, 'class': 'dws-input'}))
    salary = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'class': 'dws-input'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'required': False, 'class': 'dws-input'}))
    passport_data = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'required': False, 'class': 'dws-input'}))
    work_status = forms.CharField(max_length=24, widget=forms.TextInput(attrs={'required': False, 'class': 'dws-input'}))
    the_foremost_place_of_work = forms.ModelChoiceField(queryset=TranscendingWork.objects.all(), widget=forms.Select(attrs={'required': False, 'class': 'dws-input'}))

class ExcursionForm(forms.Form):
    price = forms.CharField(widget=forms.TextInput(attrs={'required': False, 'class': 'dws-input'}))
    start_of_route = forms.ModelChoiceField(queryset=Route.objects.all(), widget=forms.Select(attrs={'required': False, 'class': 'dws-input'}))
    number_of_seats = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'required': False, 'class': 'dws-input'}))

class UpdateSalaryForm(forms.Form):
    new_salary = forms.IntegerField( widget=forms.NumberInput(attrs={'required': False, 'class': 'dws-input'}))
    staff = forms.ModelChoiceField(queryset=Staff.objects.all(),widget=forms.Select( attrs={'required': False, 'class': 'dws-input'}))

class UpdateExcursionPrcie(forms.Form):
    new_price = forms.IntegerField( widget=forms.NumberInput(attrs={'required': False, 'class': 'dws-input'}))
    excursion = forms.ModelChoiceField(queryset=Excursion.objects.all(),widget=forms.Select( attrs={'required': False, 'class': 'dws-input'}))

class AddSightForm(forms.Form):
    name_of_attraction = forms.CharField(max_length=160, widget=forms.TextInput(attrs={'required': False, 'class': 'dws-input'}))
    description_of_attraction = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'required': False, 'class': 'dws-input'}))

class RecruitDriverForm(forms.Form):
    id_staff = forms.ModelChoiceField(queryset=Staff.objects.filter(dolzhnost='водитель').all(), widget=forms.Select(attrs={'required': False, 'class': 'dws-input'}))
    id_excursion = forms.ModelChoiceField(widget=forms.Select( attrs={'required': False, 'class': 'dws-input'}),queryset=Excursion.objects.all())

class CreateWayForm(forms.Form):
    route_name = forms.CharField(max_length=160, widget=forms.TextInput(attrs={'required': False, 'class': 'dws-input'}))
    location_on_the_route = forms.ModelChoiceField(widget=forms.Select( attrs={'required': False, 'class': 'dws-input'}),queryset=Attraction.objects.all())
    next_attraction =  forms.ModelChoiceField(widget=forms.Select(attrs={'required': False, 'class': 'dws-input'}),queryset=Route.objects.all())
    transition_time_in_minutes = forms.IntegerField( widget=forms.NumberInput(attrs={'required': False, 'class': 'dws-input'}))
    transport_delivered_to_the_sights = forms.ModelChoiceField(widget=forms.Select(attrs={'required': False, 'class': 'dws-input'}),queryset=TypesOfTransport.objects.all() )

class RemoveStaffForm(forms.Form):
    full_name = forms.ModelChoiceField(widget=forms.Select(attrs={'required': False, 'class': 'dws-input'}),queryset=Staff.objects.all())

class GetListForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'required': False, 'class': 'dws-input'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'required': False, 'class': 'dws-input'}))

class OrderExcursion(forms.Form):
    id_excursion = forms.ModelChoiceField(queryset=Excursion.objects.all(), widget=forms.Select(attrs={'required': False, 'class': 'dws-input'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'required': False, 'class': 'dws-input'}))

class OrderGid(forms.Form):
    id_staff = forms.ModelChoiceField(queryset=Staff.objects.filter(dolzhnost='гид').all(), widget=forms.Select(attrs={'required': False, 'class': 'dws-input'}))
    id_excursion = forms.ModelChoiceField(widget=forms.Select( attrs={'required': False, 'class': 'dws-input'}),queryset=Excursion.objects.all())

