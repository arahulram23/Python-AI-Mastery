name = input("Enter your name: ")
age =  int(input("Enter your age:"))
cgpa = float(input("Enter your CGPA:"))
placement_status = input("Enter your placement status (True/False):").lower()=="true"

profile = f"""
Profile
-------------------------
Name: {name}
Age: {age}
CGPA: {cgpa}
Placement Status: {placement_status}
"""

print(profile)