from django.db import models

# Create your models here.
class patient(models.Model):
    firstname = models.CharField(max_length= 20)
    surname = models.CharField(max_length= 20)
    age = models.IntegerField()
    dob = models.DateField()
    phone = models.CharField(max_length=10)
    visitdate = models.DateTimeField()
    medicalhistory = models.TextField()

    def __str__(self):
        return self.firstname + " " + self.surname


class MedicalRecords(models.Model):
    patientname = models.CharField(max_length=20)
    doctor = models.CharField(max_length=50)
    diagnosis = models.TextField()
    email = models.EmailField()
  
    def __str__(self):
        return self.patientname


class Appointment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    datetime = models.DateTimeField()
    department = models.CharField(max_length=20)
    doctor = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
