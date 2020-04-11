from django.shortcuts import render
from .models import DoctorData, NurseData, PatientData

def index(request):
    return render(request, 'hms/index.html') 

def doctor(request):
	return render(request, 'hms/doctor.html')

def doctor_data_submit(request):
	print("Data Submitted")
	doctor_fname = request.POST["doctor_fname"]
	doctor_lname = request.POST["doctor_lname"]


	doctor_info = DoctorData(doctor_fname=doctor_fname, doctor_lname=doctor_lname)
	doctor_info.save()

	return render(request, 'hms/doctor.html')

def doctor_list(request):
	doctor_list = DoctorData.objects.all()

	return render(request, 'hms/doctor_list.html', {'doctor_list':doctor_list})

def nurse(request):
	return render(request, 'hms/nurse.html')

def nurse_data_submit(request):
	print("Data Submitted")
	nurse_fname = request.POST["nurse_fname"]
	nurse_lname = request.POST["nurse_lname"]

	nurse_shift_type = request.POST.get('nurse_shift_type', None)
	print(nurse_shift_type)

	doctor_assigned = DoctorData.objects.get(doctor_fname=nurse_shift_type)
	
	nurse_info = NurseData(nurse_fname=nurse_fname, nurse_lname=nurse_lname, doctor_fk=doctor_assigned)
	nurse_info.save()
	
	return render(request, 'hms/nurse.html')


def nurse_list(request):
	nurse_list = NurseData.objects.all()

	return render(request, 'hms/nurse_list.html', {'nurse_list':nurse_list})

def patient(request):
	return render(request, 'hms/patient.html')

def patient_data_submit(request):
	patient_fname = request.POST["patient_fname"]
	patient_lname = request.POST["patient_lname"]
	patient_diagnosis = request.POST["patient_diagnosis"]

	nurse_assigned = NurseData.objects.get(nurse_fname=patient_lname)
	doctor_assigned = DoctorData.objects.get(doctor_fname=patient_diagnosis)

	patient_info = PatientData(patient_fname=patient_fname, nurse_fk=nurse_assigned, patient_doctor_fk=doctor_assigned)
	patient_info.save()

	return render(request,'hms/patient.html')

def patient_list(request):
	patient_list = PatientData.objects.all()

	return render(request, 'hms/patient_list.html', {'patient_list':patient_list})