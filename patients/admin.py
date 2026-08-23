from django.contrib import admin
from .models import Appointment, Doctor, Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("name","age","gender","phone","email")
    search_fields = ("name","phone","email")
    list_filter = ("gender",)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name","specialization","phone","experience")
    search_fields = ("name","specialization","phone")
    list_filter = ("specialization",)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("patient","doctor","appointment_date","appointment_time","status")
    search_fields = ("patient__name","doctor__name","reason")
    list_filter = ("status","appointment_date")
