from django.contrib import admin
from django.urls import path

from patients import views


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'patients/',
        views.patient_list,
        name='patient_list'
    ),

    path(
        'patients/add/',
        views.add_patient,
        name='add_patient'
    ),

    path(
        'patients/edit/<int:id>/',
        views.edit_patient,
        name='edit_patient'
    ),

    path(
        'patients/delete/<int:id>/',
        views.delete_patient,
        name='delete_patient'
    ),

    path(
        'doctors/',
        views.doctor_list,
        name='doctor_list'
    ),

    path(
        'doctors/add/',
        views.add_doctor,
        name='add_doctor'
    ),

    path(
        'doctors/edit/<int:id>/',
        views.edit_doctor,
        name='edit_doctor'
    ),

    path(
        'doctors/delete/<int:id>/',
        views.delete_doctor,
        name='delete_doctor'
    ),

    path(
        'appointments/',
        views.appointment_list,
        name='appointment_list'
    ),

    path(
        'appointments/add/',
        views.add_appointment,
        name='add_appointment'
    ),

    path(
        'appointments/delete/<int:id>/',
        views.delete_appointment,
        name='delete_appointment'
    ),

]