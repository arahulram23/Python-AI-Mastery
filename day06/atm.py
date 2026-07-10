balance = 5000

print ("Welcome to ATM")
print ("1. Check Balance")
print("2. Withdraw Money")
print("3. Deposit Money")

choice = int(input("Enter your choice:"))

if choice == 1:
    print("Your balance is: ", balance)
elif choice ==2:
    withdraw_amount = float(input("Enter amount to withdraw: "))
    if withdraw_amount <= balance:
        balance -= withdraw_amount
        print("Withdrawal successful. New balance is: ", balance)
    else:
        print("Insufficient balance:")
elif choice == 3:
    deposit_amount = float(input("Enter amount to deposit:"))
    balance += deposit_amount
    print("Deposit successful. New balance is: ", balance)
else:
    print("Invalid choice. Please try again.")
