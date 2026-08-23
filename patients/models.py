from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [("Male","Male"),("Female","Female"),("Other","Other")]
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=120)
    specialization = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    experience = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return f"Dr. {self.name}"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ("Scheduled","Scheduled"),("Completed","Completed"),("Cancelled","Cancelled")
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Scheduled")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-appointment_date", "-appointment_time"]
    def __str__(self):
        return f"{self.patient} - {self.doctor} - {self.appointment_date}"
