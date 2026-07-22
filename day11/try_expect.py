try:
    num = int(input("Enter a number: "))
    print(f"100/ {num}")
except ValueError:
    print("That's not a valid number. Please enter an integer.")
except ZeroDivisionError:
    print("You cannot divide by zero. Please enter a non-zero integer.")

try:
    num = int(input("Enter another number: "))
    print(f"100/ {num}")
except exception as e:
    print(f"An error occurred: {e}")


age = input("Enter your age: ")
if age<18:
    raise ValueError("Age must be 18 or older.")