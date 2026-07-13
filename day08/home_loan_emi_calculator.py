import math

def home_loan_calculator():
    print("=" * 45)
    print("         HOME LOAN EMI CALCULATOR")
    print("=" * 45)

    loan_amount = float(input("Enter Loan Amount (₹): "))
    annual_interest = float(input("Enter Annual Interest Rate (%): "))
    tenure_years = int(input("Enter Loan Tenure (Years): "))

    monthly_rate = annual_interest / (12 * 100)
    tenure_months = tenure_years * 12

    emi = (
        loan_amount
        * monthly_rate
        * math.pow(1 + monthly_rate, tenure_months)
    ) / (
        math.pow(1 + monthly_rate, tenure_months) - 1
    )

    total_payment = emi * tenure_months
    total_interest = total_payment - loan_amount

    print("\n========== LOAN SUMMARY ==========")
    print(f"Loan Amount      : ₹{loan_amount:,.2f}")
    print(f"Interest Rate    : {annual_interest:.2f}%")
    print(f"Loan Tenure      : {tenure_years} Years")
    print(f"Monthly EMI      : ₹{emi:,.2f}")
    print(f"Total Interest   : ₹{total_interest:,.2f}")
    print(f"Total Payment    : ₹{total_payment:,.2f}")

if __name__ == "__main__":
    home_loan_calculator()