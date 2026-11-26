# Personal Budget Calculator

salary = float(input("Enter your monthly salary: "))

rent = float(input("Enter your monthly rent: "))

groceries = float(input("Enter your monthly grocery expenses: "))

remaining = salary - rent - groceries

print("Money remaining:", remaining)

if remaining >= 0:

    print("You are within budget!")

else:

    print("You are overspending!")