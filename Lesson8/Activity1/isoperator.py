num1= int(input("Enter your age?"))

if type(num1) is int:
    print("It is an integer")
if type(num1) is not int:
    print("It is not an integer")

print("I will verify if your honest or not.")

num2= int(input("What is your age?"))
if num1 is num2:
    print("You are very honest")
else:
    print("Liar")