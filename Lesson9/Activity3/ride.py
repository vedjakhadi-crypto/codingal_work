print("Welcome to the ride experience")

print("Select one of the options :")
print("1 for bike")
print("2 for car")

choice = int(input("Pick one option"))

if (choice ==1):
    print("Would you want to ride a dirt bike or a sport bike?")
    print("1.1 for dirt bike")
    print("1.2 for sport bike")
    choice2 = float(input("Pick one option"))
    if (choice2 == 1.1):
        print("You have chosen to ride a Dirt bike!")
    elif(choice2 ==  1.2):
        print("You have chosen to ride a Sport bike!")
    else:
         print("Not a valid choice")
elif(choice == 2):
    print("Would you want to ride a F1car or a Tesla Roadster?")
    print("2.1 for F1car")
    print("2.2 for Tesla Roadster")
    choice2 = float(input("Pick one option"))
    if (choice2 == 2.1):
          print("You have chosen to ride a F1car!")
    elif(choice2 == 2.2):
          print("You have chosen to ride a Tesla Roadster!")
    else:
         print("Not a valid choice")
else:
     print("Your choice is not valid.")