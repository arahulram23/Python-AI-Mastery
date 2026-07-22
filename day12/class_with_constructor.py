class Patient:
    def __init__(self, name, age, sex):
        self.name = name
        self.age=age
        self.sex=sex

patient = Patient("John Doe", 30, "Male")

print(patient.name)
print(patient.age)
print(patient.sex)

