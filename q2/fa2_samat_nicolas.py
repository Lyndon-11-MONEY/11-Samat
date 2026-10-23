'''
Lyndon John F Nicolas
9-Samat
‎Oct. 16, 2026
‎'''
class Patient:
    def __init__(self, name, bill_amount=0):
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

class Senior(Patient):
    def __init__(self, name, sdiscount = 0.20, bill_amount = 0):
        super().__init__(name, bill_amount)
        self.sdiscount = sdiscount
   
    def get_sdiscount(self, sdiscount):
        return self.sdiscount
   
    def set_sdiscount(self, sdiscount):
        self.sdiscount = sdiscount
   
    def set_bill_amount(self):
        self.bill_amount
        return self.bill_amount
   
    def calculate_bill(self):
        discount_amount = self.bill_amount * self.sdiscount
        return self.bill_amount - discount_amount

class PhilHealth(Patient):
    def __init__(self, name, pdiscount = 0.15, bill_amount = 0):
        super().__init__(name, bill_amount)
        self.pdiscount = pdiscount
   
    def set_pdiscount(self, pdiscount):
        self.pdiscount = pdiscount
   
    def set_bill_amount(self):
        self.bill_amount
        return self.bill_amount
   
    def calculate_bill(self):
        discount_amount = self.bill_amount * self.pdiscount
        return self.bill_amount - discount_amount



print("Hospital Billing System")
print("----------------------")

regular_patient = Patient("Juan Dela Cruz", bill_amount = 15000.00)
print("Patient Name: ", regular_patient.get_name())
print("Original Bill: ", "₱", f"{regular_patient.get_bill_amount():.2f}")
print("Final Bill: ", "₱", f"{regular_patient.calculate_bill():.2f}")

print(" ")

senior_patient = Senior("Maria Santos", bill_amount = 15000.00)
print("Patient Name: ", senior_patient.get_name())
print("Original Bill: ", "₱", f"{senior_patient.get_bill_amount():.2f}")
print("Final Bill: ", "₱", f"{senior_patient.calculate_bill():.2f}")

print(" ")

philhealth_patient = PhilHealth("Maria Santos", bill_amount = 15000.00)
print("Patient Name: ", philhealth_patient.get_name())
print("Original Bill: ", "₱", f"{philhealth_patient.get_bill_amount():.2f}")
print("Final Bill: ", "₱", f"{philhealth_patient.calculate_bill():.2f}")


