from django.db import models

# Create your models here.
class Record(models.Model):
    patient_name = models.CharField(max_length=255)
    patient_phone = models.CharField(max_length=255)
    patient_address = models.TextField()
    patient_case = models.TextField()
    drug = models.TextField()
    fees = models.DecimalField(max_digits=9, decimal_places=2)
    doctor = models.CharField(max_length=255)
    date = models.DateField() 

    def __str__(self):
        return self.patient_name