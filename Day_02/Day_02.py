print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip you would like to give? 10, 12 or 15 "))
split = int(input("How many people to split the bill? "))

total_bill = bill + (bill * tip / 100)
each_person = total_bill / split
final_bill = round(each_person, 2)

print(f"Each person should pay: ${final_bill}")
