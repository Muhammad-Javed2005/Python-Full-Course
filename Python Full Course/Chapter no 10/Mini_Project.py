from abc import ABC, abstractmethod

# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_profile(self):
        return f"{self.name}, Age: {self.age}"

# Appointment abstract class
class Appointment(ABC):
    @abstractmethod
    def book_appointment(self):
        pass

# Doctor class
class Doctor(Person):
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty
        self.patients = []

    def show_profile(self):
        return f"Dr. {self.name} (Specialist: {self.specialty})"

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"{patient.name} added to Dr. {self.name}'s list.")

    def write_report(self, patient, report):
        patient._add_medical_record(report)
        print(f"Report written for {patient.name}.")

# Patient class
class Patient(Person, Appointment):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__medical_history = []
        self.doctor = None

    def book_appointment(self, doctor: Doctor):
        self.doctor = doctor
        doctor.add_patient(self)

    def view_history(self):
        print(f"Medical History for {self.name}:")
        for entry in self.__medical_history:
            print("-", entry)

    def _add_medical_record(self, entry):
        self.__medical_history.append(entry)

# Admin class
class Admin(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def show_all_doctors(self, hospital):
        print("\n--- List of Doctors ---")
        for doc in hospital.doctors:
            print(doc.show_profile())

    def show_all_patients(self, hospital):
        print("\n--- List of Patients ---")
        for pat in hospital.patients:
            print(pat.show_profile())

# Composition class: Hospital


class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def system_summary(self):
        print(f"\nHospital: {self.name}")
        print(f"Total Doctors: {len(self.doctors)}")
        print(f"Total Patients: {len(self.patients)}")

# === TESTING THE PROJECT ===

# Creating hospital
hosp = Hospital("Care & Cure Hospital")

# Creating doctors
doc1 = Doctor("Imran", 50, "Cardiology")
doc2 = Doctor("Sara", 42, "Neurology")
hosp.add_doctor(doc1)
hosp.add_doctor(doc2)

# Creating patients
pat1 = Patient("Ali", 30)
pat2 = Patient("Fatima", 25)
hosp.add_patient(pat1)
hosp.add_patient(pat2)

# Booking appointments
pat1.book_appointment(doc1)
pat2.book_appointment(doc2)

# Doctors writing reports
doc1.write_report(pat1, "Diagnosed with mild hypertension")
doc2.write_report(pat2, "MRI recommended for headaches")

# Viewing history
pat1.view_history()
pat2.view_history()

# Admin functionalities
admin = Admin("Mr. Kamran", 40)
admin.show_all_doctors(hosp)
admin.show_all_patients(hosp)

# Summary
hosp.system_summary()


print("This program was developed by Engr. Muhammad Javed.")

