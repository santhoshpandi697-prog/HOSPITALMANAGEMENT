from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Patient, Doctor, Appointment
from .forms import PatientForm, DoctorForm


# =========================
# DASHBOARD
# =========================

def dashboard(request):

    patients_count = Patient.objects.count()
    doctors_count = Doctor.objects.count()
    appointments_count = Appointment.objects.count()

    today = timezone.localdate()

    today_appointments = Appointment.objects.filter(
        appointment_date=today
    ).count()

    recent_appointments = Appointment.objects.select_related(
        'patient',
        'doctor'
    ).order_by(
        '-appointment_date',
        '-appointment_time'
    )[:5]

    return render(
        request,
        'patients/dashboard.html',
        {
            'patients_count': patients_count,
            'doctors_count': doctors_count,
            'appointments_count': appointments_count,
            'today_appointments': today_appointments,
            'recent_appointments': recent_appointments,
        }
    )


# =========================
# PATIENTS
# =========================

def patient_list(request):

    patients = Patient.objects.all()

    search = request.GET.get('search', '')
    gender = request.GET.get('gender', '')

    if search:
        patients = patients.filter(
            name__icontains=search
        )

    if gender:
        patients = patients.filter(
            gender__iexact=gender
        )

    return render(
        request,
        'patients/patient_list.html',
        {
            'patients': patients,
            'search': search,
            'gender': gender,
        }
    )


def add_patient(request):

    if request.method == 'POST':

        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('patient_list')

    else:
        form = PatientForm()

    return render(
        request,
        'patients/add_patient.html',
        {
            'form': form
        }
    )


def edit_patient(request, id):

    patient = get_object_or_404(
        Patient,
        id=id
    )

    if request.method == 'POST':

        form = PatientForm(
            request.POST,
            instance=patient
        )

        if form.is_valid():
            form.save()
            return redirect('patient_list')

    else:

        form = PatientForm(
            instance=patient
        )

    return render(
        request,
        'patients/edit_patient.html',
        {
            'form': form,
            'patient': patient
        }
    )


def delete_patient(request, id):

    patient = get_object_or_404(
        Patient,
        id=id
    )

    if request.method == 'POST':

        patient.delete()
        return redirect('patient_list')

    return render(
        request,
        'patients/delete_patient.html',
        {
            'patient': patient
        }
    )


# =========================
# DOCTORS
# =========================

def doctor_list(request):

    doctors = Doctor.objects.all()

    search = request.GET.get('search', '')
    specialization = request.GET.get(
        'specialization',
        ''
    )

    if search:

        doctors = doctors.filter(
            name__icontains=search
        )

    if specialization:

        doctors = doctors.filter(
            specialization__iexact=specialization
        )

    specializations = Doctor.objects.values_list(
        'specialization',
        flat=True
    ).distinct()

    return render(
        request,
        'patients/doctor_list.html',
        {
            'doctors': doctors,
            'search': search,
            'specialization': specialization,
            'specializations': specializations,
        }
    )


def add_doctor(request):

    if request.method == 'POST':

        form = DoctorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('doctor_list')

    else:

        form = DoctorForm()

    return render(
        request,
        'patients/add_doctor.html',
        {
            'form': form
        }
    )


def edit_doctor(request, id):

    doctor = get_object_or_404(
        Doctor,
        id=id
    )

    if request.method == 'POST':

        form = DoctorForm(
            request.POST,
            instance=doctor
        )

        if form.is_valid():
            form.save()
            return redirect('doctor_list')

    else:

        form = DoctorForm(
            instance=doctor
        )

    return render(
        request,
        'patients/edit_doctor.html',
        {
            'form': form,
            'doctor': doctor
        }
    )


def delete_doctor(request, id):

    doctor = get_object_or_404(
        Doctor,
        id=id
    )

    if request.method == 'POST':

        doctor.delete()
        return redirect('doctor_list')

    return render(
        request,
        'patients/delete_doctor.html',
        {
            'doctor': doctor
        }
    )


# =========================
# APPOINTMENTS
# =========================

def appointment_list(request):

    appointments = Appointment.objects.select_related(
        'patient',
        'doctor'
    ).all().order_by(
        '-appointment_date',
        '-appointment_time'
    )

    status = request.GET.get('status', '')
    search = request.GET.get('search', '')

    if status:

        appointments = appointments.filter(
            status__iexact=status
        )

    if search:

        appointments = appointments.filter(
            patient__name__icontains=search
        )

    return render(
        request,
        'patients/appointment_list.html',
        {
            'appointments': appointments,
            'status': status,
            'search': search,
        }
    )


def add_appointment(request):

    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    if request.method == 'POST':

        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        appointment_date = request.POST.get(
            'appointment_date'
        )
        appointment_time = request.POST.get(
            'appointment_time'
        )
        reason = request.POST.get('reason')
        status = request.POST.get('status')

        Appointment.objects.create(
            patient_id=patient_id,
            doctor_id=doctor_id,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            reason=reason,
            status=status
        )

        return redirect('appointment_list')

    return render(
        request,
        'patients/add_appointment.html',
        {
            'patients': patients,
            'doctors': doctors
        }
    )


def delete_appointment(request, id):

    appointment = get_object_or_404(
        Appointment,
        id=id
    )

    if request.method == 'POST':

        appointment.delete()
        return redirect('appointment_list')

    return render(
        request,
        'patients/delete_appointment.html',
        {
            'appointment': appointment
        }
    )