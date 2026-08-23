from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Doctor",
            fields=[
                ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
                ("name",models.CharField(max_length=120)),("specialization",models.CharField(max_length=120)),
                ("phone",models.CharField(max_length=20)),("email",models.EmailField(blank=True,max_length=254)),
                ("experience",models.PositiveIntegerField(default=0)),("created_at",models.DateTimeField(auto_now_add=True)),
            ], options={"ordering":["name"]},
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
                ("name",models.CharField(max_length=120)),("age",models.PositiveIntegerField()),
                ("gender",models.CharField(choices=[("Male","Male"),("Female","Female"),("Other","Other")],max_length=10)),
                ("phone",models.CharField(max_length=20)),("email",models.EmailField(blank=True,max_length=254)),
                ("address",models.TextField(blank=True)),("created_at",models.DateTimeField(auto_now_add=True)),
            ], options={"ordering":["name"]},
        ),
        migrations.CreateModel(
            name="Appointment",
            fields=[
                ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
                ("appointment_date",models.DateField()),("appointment_time",models.TimeField()),
                ("reason",models.CharField(max_length=255)),
                ("status",models.CharField(choices=[("Scheduled","Scheduled"),("Completed","Completed"),("Cancelled","Cancelled")],default="Scheduled",max_length=20)),
                ("notes",models.TextField(blank=True)),("created_at",models.DateTimeField(auto_now_add=True)),
                ("doctor",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="appointments",to="patients.doctor")),
                ("patient",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="appointments",to="patients.patient")),
            ], options={"ordering":["-appointment_date","-appointment_time"]},
        ),
    ]
