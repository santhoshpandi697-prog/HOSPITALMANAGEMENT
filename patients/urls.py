from django.urls import path
from .views import (
    DashboardView, PatientListView, PatientCreateView, PatientUpdateView, PatientDeleteView,
    DoctorListView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView,
    AppointmentListView, AppointmentCreateView, AppointmentUpdateView, AppointmentDeleteView,
)
urlpatterns = [
    path("", DashboardView.as_view(), name="home"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("patients/", PatientListView.as_view(), name="patient_list"),
    path("patients/add/", PatientCreateView.as_view(), name="add_patient"),
    path("patients/edit/<int:pk>/", PatientUpdateView.as_view(), name="edit_patient"),
    path("patients/delete/<int:pk>/", PatientDeleteView.as_view(), name="delete_patient"),
    path("doctors/", DoctorListView.as_view(), name="doctor_list"),
    path("doctors/add/", DoctorCreateView.as_view(), name="add_doctor"),
    path("doctors/edit/<int:pk>/", DoctorUpdateView.as_view(), name="edit_doctor"),
    path("doctors/delete/<int:pk>/", DoctorDeleteView.as_view(), name="delete_doctor"),
    path("appointments/", AppointmentListView.as_view(), name="appointment_list"),
    path("appointments/add/", AppointmentCreateView.as_view(), name="add_appointment"),
    path("appointments/edit/<int:pk>/", AppointmentUpdateView.as_view(), name="edit_appointment"),
    path("appointments/delete/<int:pk>/", AppointmentDeleteView.as_view(), name="delete_appointment"),
]
