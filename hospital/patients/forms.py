from django import forms
from .models import Patient, Doctor


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'