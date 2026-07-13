def property_valuation(monthly_rent):
    annual_rent = monthly_rent * 12

    better_price = annual_rent / 0.035   # 3.5% yield
    fair_price = annual_rent / 0.025     # 2.5% yield

    print("\n========== PROPERTY VALUATION ==========")
    print(f"Monthly Rent : ₹{monthly_rent:,.0f}")
    print(f"Annual Rent  : ₹{annual_rent:,.0f}\n")

    print("Recommended Property Price:")
    print(f"✅ Better-priced property (Yield > 3.5%) : Up to ₹{better_price:,.0f}")
    print(f"🟡 Fair valuation (2.5% - 3.5%)         : ₹{better_price:,.0f} - ₹{fair_price:,.0f}")
    print(f"🔴 Higher-priced property               : Above ₹{fair_price:,.0f}")


# Main Program
monthly_rent = float(input("Enter Monthly Rent (₹): "))
property_valuation(monthly_rent)