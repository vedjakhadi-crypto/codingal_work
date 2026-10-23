print("Welcome to your mood advisor ")

name = input("What is your name? ")
mood = input("How are you feeling today? ")
energy = int(input("What is your energy level from 1-10(1 is very dull and 10 is fantastic)? "))

if energy <= 3:
    print("Eat something that you like to make you feel better")

if energy <= 5:
    print("Just rest for today!")
else:
    print("Do something productive today")
print("Also, have a great day")
