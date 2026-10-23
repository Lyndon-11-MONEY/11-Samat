'''
Lyndon John F Nicolas
9-Samat
‎Oct. 16, 2026
‎'''
class Patient:
    def __init__(self, name, bill_amount): #no discount
        self.name = name
        self.bill_amount = bill_amount
   
    def get_name(self):
        return self.name
   
    def set_name(self, name):
        self.name = name
   
    def get_bill_amount(self):
        self.bill_amount
        return self.bill_amount
   
    def calculate_bill(self):
        return self.bill_amount

class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80 # 20% discount


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85 # 15% discount
        
#thing getting printed
print("Hospital Billing System")
print("------------------------")

regular_patient = Patient("Juan Dela Cruz", bill_amount = 15000.00)
print("Patient Name: ", regular_patient.get_name())
print("Original Bill: ", "₱", f"{regular_patient.get_bill_amount():}")
print("Final Bill: ", "₱", f"{regular_patient.calculate_bill():}")

print(" ")

senior_patient = SeniorPatient("Maria Santos", bill_amount = 15000.00)
print("Patient Name: ", senior_patient.get_name())
print("Original Bill: ", "₱", f"{senior_patient.get_bill_amount():}")
print("Final Bill: ", "₱", f"{senior_patient.calculate_bill():}")

print(" ")

philhealth_patient = PhilHealthPatient("Maria Santos", bill_amount = 15000.00)
print("Patient Name: ", philhealth_patient.get_name())
print("Original Bill: ", "₱", f"{philhealth_patient.get_bill_amount():}")
print("Final Bill: ", "₱", f"{philhealth_patient.calculate_bill():}")
