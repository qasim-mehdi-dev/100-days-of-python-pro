print("Welcome to Rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 13:
        print("Children ticket costs 5$")
        bill += 5
    elif age <= 18:
        print("Youth ticket costs 7$")
        bill += 7
    elif 45 <= age <= 55:
        print("Don't worry everything is going to be fine, Your ticket is free")
        bill += 0
    else:
        print("Adult ticket costs 12$")
        bill += 12
    photo_both = input("Do you want to take a photo? (y/n): ")
    if photo_both == "y":
        bill += 3
    print(f"Your final bill is: {bill}")
else:
    print("Sorry, come back when you are taller.")
















