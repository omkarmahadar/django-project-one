from django.db import models

class DoctorData(models.Model):
	doctor_fname = models.CharField(max_length=255, null=True, blank=True)		#1
	doctor_lname = models.CharField(max_length=255, null=True, blank=True)		#2
	doctor_salary = models.IntegerField(null=True, blank=True)					#3
	doctor_qualification = models.CharField(max_length=255, null=True, blank=True)#4
	doctor_phone_no = models.CharField(max_length=12, null=True, blank=True)	#5
	doctor_shift_type = models.CharField(max_length=255, null=True, blank=True)	#6

	def __str__(self):
		return self.doctor_fname

class NurseData(models.Model):
	nurse_fname = models.CharField(max_length=255, null=True, blank=True)
	nurse_lname = models.CharField(max_length=255, null=True, blank=True)
	nurse_salary = models.IntegerField(null=True, blank=True)
	nurse_shift_type = models.CharField(max_length=255, null=True, blank=True)
	nurse_shift_duration = models.IntegerField(null=True, blank=True)

	doctor_fk = models.ForeignKey('DoctorData', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.nurse_fname

class PatientData(models.Model):
	patient_fname = models.CharField(max_length=255, null=True, blank=True)
	patient_lname = models.CharField(max_length=255, null=True, blank=True)
	patient_age = models.IntegerField(null=True, blank=True)
	patient_phone_no = models.CharField(max_length=12, null=True, blank=True)
	patient_relative_ph_no = models.CharField(max_length=12, null=True, blank=True)
	patient_diagnosis = models.CharField(max_length=255, null=True, blank=True)

	nurse_fk = models.ForeignKey('NurseData', on_delete=models.CASCADE, null=True, blank=True)
	patient_doctor_fk = models.ForeignKey('DoctorData', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.patient_fname