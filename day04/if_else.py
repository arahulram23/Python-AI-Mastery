# if else statement
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote!!!")
else:
    print("Not eligible to vote!!!")

mark = int(input("Enter your marks:"))

if mark >= 90:
    print("Grade A")
elif mark >= 80:
    print("Grade B")
elif mark >=70:
    print("Grade C")
elif mark >= 60:
    print("Grade D")
elif mark >= 35:
    print("Grade E")
else:
    print("Fail")