import csv

expenses = [
    {
        "name":"Dosa",
        "category":"Food",
        "amount": 100
    },
    {
        "name" : "Biscuits",
        "category":"Snacks",
        "amount": 50
    }
]

with open("expenses.csv","w") as file:
    fieldname=["name", "category", "amount"]
    writer = csv.DictWriter(file, fieldnames=fieldname)
    writer.writeheader()
    writer.writerows(expenses)
