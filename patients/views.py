from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView
from .forms import AppointmentForm, DoctorForm, PatientForm
from .models import Appointment, Doctor, Patient

class DashboardView(TemplateView):
    template_name = "patients/dashboard.html"
    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        today = timezone.localdate()
        c.update(
            patients_count=Patient.objects.count(),
            doctors_count=Doctor.objects.count(),
            appointments_count=Appointment.objects.count(),
            today_appointments=Appointment.objects.filter(appointment_date=today).count(),
            recent_appointments=Appointment.objects.select_related("patient","doctor").order_by(
                "-appointment_date","-appointment_time"
            )[:6],
        )
        return c

class PatientListView(ListView):
    model = Patient
    template_name = "patients/patient_list.html"
    context_object_name = "patients"
    paginate_by = 10
    def get_queryset(self):
        q = Patient.objects.all()
        s = self.request.GET.get("search","").strip()
        g = self.request.GET.get("gender","").strip()
        if s:
            q = q.filter(Q(name__icontains=s)|Q(phone__icontains=s)|Q(email__icontains=s))
        if g: q = q.filter(gender=g)
        return q
    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c["search"] = self.request.GET.get("search","")
        c["gender"] = self.request.GET.get("gender","")
        return c

class PatientCreateView(CreateView):
    model = Patient; form_class = PatientForm; template_name = "patients/form.html"; success_url = reverse_lazy("patient_list")
    extra_context = {"title":"Add Patient","subtitle":"Create a new patient record.","back_url":"patient_list"}
    def form_valid(self, form):
        messages.success(self.request,"Patient added successfully."); return super().form_valid(form)

class PatientUpdateView(UpdateView):
    model = Patient; form_class = PatientForm; template_name = "patients/form.html"; success_url = reverse_lazy("patient_list")
    extra_context = {"title":"Edit Patient","subtitle":"Update patient information.","back_url":"patient_list"}
    def form_valid(self, form):
        messages.success(self.request,"Patient updated successfully."); return super().form_valid(form)

class PatientDeleteView(DeleteView):
    model = Patient; template_name = "patients/confirm_delete.html"; success_url = reverse_lazy("patient_list")
    extra_context = {"item_type":"patient"}
    def form_valid(self, form):
        messages.success(self.request,"Patient deleted successfully."); return super().form_valid(form)

class DoctorListView(ListView):
    model = Doctor
    template_name = "patients/doctor_list.html"
    context_object_name = "doctors"
    paginate_by = 10
    def get_queryset(self):
        q = Doctor.objects.all()
        s = self.request.GET.get("search","").strip()
        sp = self.request.GET.get("specialization","").strip()
        if s: q = q.filter(Q(name__icontains=s)|Q(phone__icontains=s)|Q(email__icontains=s))
        if sp: q = q.filter(specialization=sp)
        return q
    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c["search"] = self.request.GET.get("search","")
        c["specialization"] = self.request.GET.get("specialization","")
        c["specializations"] = Doctor.objects.values_list("specialization",flat=True).distinct().order_by("specialization")
        return c

class DoctorCreateView(CreateView):
    model = Doctor; form_class = DoctorForm; template_name = "patients/form.html"; success_url = reverse_lazy("doctor_list")
    extra_context = {"title":"Add Doctor","subtitle":"Create a new doctor profile.","back_url":"doctor_list"}
    def form_valid(self, form):
        messages.success(self.request,"Doctor added successfully."); return super().form_valid(form)

class DoctorUpdateView(UpdateView):
    model = Doctor; form_class = DoctorForm; template_name = "patients/form.html"; success_url = reverse_lazy("doctor_list")
    extra_context = {"title":"Edit Doctor","subtitle":"Update doctor information.","back_url":"doctor_list"}
    def form_valid(self, form):
        messages.success(self.request,"Doctor updated successfully."); return super().form_valid(form)

class DoctorDeleteView(DeleteView):
    model = Doctor; template_name = "patients/confirm_delete.html"; success_url = reverse_lazy("doctor_list")
    extra_context = {"item_type":"doctor"}
    def form_valid(self, form):
        messages.success(self.request,"Doctor deleted successfully."); return super().form_valid(form)

class AppointmentListView(ListView):
    model = Appointment
    template_name = "patients/appointment_list.html"
    context_object_name = "appointments"
    paginate_by = 10
    def get_queryset(self):
        q = Appointment.objects.select_related("patient","doctor").all()
        st = self.request.GET.get("status","").strip()
        s = self.request.GET.get("search","").strip()
        if st: q = q.filter(status=st)
        if s:
            q = q.filter(Q(patient__name__icontains=s)|Q(doctor__name__icontains=s)|Q(reason__icontains=s))
        return q
    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c["status"] = self.request.GET.get("status","")
        c["search"] = self.request.GET.get("search","")
        return c

class AppointmentCreateView(CreateView):
    model = Appointment; form_class = AppointmentForm; template_name = "patients/form.html"; success_url = reverse_lazy("appointment_list")
    extra_context = {"title":"New Appointment","subtitle":"Schedule an appointment for a patient.","back_url":"appointment_list"}
    def form_valid(self, form):
        messages.success(self.request,"Appointment created successfully."); return super().form_valid(form)

class AppointmentUpdateView(UpdateView):
    model = Appointment; form_class = AppointmentForm; template_name = "patients/form.html"; success_url = reverse_lazy("appointment_list")
    extra_context = {"title":"Edit Appointment","subtitle":"Update appointment details.","back_url":"appointment_list"}
    def form_valid(self, form):
        messages.success(self.request,"Appointment updated successfully."); return super().form_valid(form)

class AppointmentDeleteView(DeleteView):
    model = Appointment; template_name = "patients/confirm_delete.html"; success_url = reverse_lazy("appointment_list")
    extra_context = {"item_type":"appointment"}
    def form_valid(self, form):
        messages.success(self.request,"Appointment deleted successfully."); return super().form_valid(form)
