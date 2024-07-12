from django.urls import path
from .views import *

app_name = 'shtraf'

urlpatterns = [
    path('leed_report_view/', leed_report_view, name='leed_report_view'),
    path('my_profile/', my_profile, name='my_profile'),
    path('doctor_search/', DoctorAutocompleteView.as_view(), name='doctor_search'),
    path('shtraf_report/', shtraf_report_view, name='shtraf_report_view'),
    path('buh_report_view/', buh_report_view, name='buh_report_view'),
    path('report_view/', report_view, name='report_view'),
    path('otdel/', otdel_list, name='otdel_list'),
    path('otdel_detail/<int:pk>/', otdel_detail, name='otdel_detail'),
    path('create_shtraf/<int:pk>/', create_shtraf, name='create_shtraf'),
    path('', profile_list, name='profile_list'),
    path('profile_detail/<int:pk>', profile_detail, name='profile_detail'),
]