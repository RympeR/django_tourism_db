from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='main_page'),
    path('index/', index,name='main_page'),

    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),

    path('recrut_driver/', recrut_driver, name='recrut_driver'),
    path('get_list/', get_list, name='get_list'),
    path('create_excursion/', create_excursion, name='create_excursion'),
    path('take_gid/', take_gid, name='take_gid'),
    path('update_salary/', update_salary, name='update_salary'),
    path('remove_staff/', remove_staff, name='remove_staff'),
    path('get_staff_list/', get_staff_list, name='get_staff_list'),
    path('recruit_staff/', recruit_staff, name='recruit_staff'),
    path('update_excursion_price/', update_excursion_price, name='update_excursion_price'),
    path('add_service/', add_service, name='add_service'),
    path('create_way/', create_way, name='create_way'),
    path('order_excursion/', order_excursion, name='order_excursion'),

    path('gid/<int:user_id>/', gid, name='gid'),
    path('client/<int:user_id>/', client, name='client'),
    path('manager/<int:user_id>/', manager, name='manager'),
    path('director/<int:user_id>/', director, name='director'),
    path('gid/<int:user_id>/', gid, name='gid'),

    path('recrut_driver_api/', RecrutDriver.as_view(), name='recrut_driver_api'),
    path('user_insert_api/', InsertUser.as_view(), name='user_insert_api'),
    path('create_way_api/', CreateWay.as_view(), name='create_way_api'),
    path('price_update_api/', UpdatePrice.as_view(), name='price_update_api'),
    path('staff_funcs_api/', StaffAPI.as_view(), name='staff_funcs_api'),
    path('service_create_api/', CreateService.as_view(), name='service_create_api'),
    path('excursion_api/', ExcursionAPI.as_view(), name='excursion_api'),
]
