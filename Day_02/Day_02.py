print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15 "))
split = int(input("How much people you would like to split the bill with? "))

total_bill = bill + (bill * tip / 100)
each_person = total_bill / split
final_amount = round(each_person, 2)

print(f"Each person should pay: {final_amount}")