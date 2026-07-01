name = input("Enter your name: ")
print(f"Hello: {name}!")

age = int(input("Enter your age: "))
if age >= 18:
    print(f"You are eligible to vote at age: {age}")
elif age < 18:
    print(f"You are not eligible to vote at age: {age}")
else:
    print("Invalid age entered. Please enter a valid age.")
    