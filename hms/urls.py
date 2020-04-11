from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'hms'

urlpatterns = [
    path('',views.index, name='home'),
    
    path('doctor/', views.doctor, name='doctor'),
    url(r'doctor_data_submit/', views.doctor_data_submit, name='doctor_data_submit'),
    path('doctor_list/', views.doctor_list, name='doctor_list'),

    path('nurse/', views.nurse, name='nurse'),
    url(r'nurse_data_submit/', views.nurse_data_submit, name='nurse_data_submit'),
	path('nurse_list/', views.nurse_list, name='nurse_list'),    

    path('patient/', views.patient, name='patient'),
    url(r'patient_data_submit/', views.patient_data_submit, name='patient_data_submit'),
    path('patient_list/', views.patient_list, name='patient_list'),

]
