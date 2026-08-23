from django import forms
from .models import Appointment, Doctor, Patient

class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

class PatientForm(StyledModelForm):
    class Meta:
        model = Patient
        fields = ["name","age","gender","phone","email","address"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder":"Full name"}),
            "age": forms.NumberInput(attrs={"placeholder":"Age","min":0}),
            "phone": forms.TextInput(attrs={"placeholder":"Phone number"}),
            "email": forms.EmailInput(attrs={"placeholder":"Email address"}),
            "address": forms.Textarea(attrs={"placeholder":"Address","rows":3}),
        }

class DoctorForm(StyledModelForm):
    class Meta:
        model = Doctor
        fields = ["name","specialization","phone","email","experience"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder":"Doctor name"}),
            "specialization": forms.TextInput(attrs={"placeholder":"e.g. Cardiology"}),
            "phone": forms.TextInput(attrs={"placeholder":"Phone number"}),
            "email": forms.EmailInput(attrs={"placeholder":"Email address"}),
            "experience": forms.NumberInput(attrs={"placeholder":"Years","min":0}),
        }

class AppointmentForm(StyledModelForm):
    class Meta:
        model = Appointment
        fields = ["patient","doctor","appointment_date","appointment_time","reason","status","notes"]
        widgets = {
            "appointment_date": forms.DateInput(attrs={"type":"date"}),
            "appointment_time": forms.TimeInput(attrs={"type":"time"}),
            "reason": forms.TextInput(attrs={"placeholder":"Reason for visit"}),
            "notes": forms.Textarea(attrs={"placeholder":"Additional notes","rows":4}),
        }
