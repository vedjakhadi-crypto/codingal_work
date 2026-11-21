print("Welcome to the calculator")

num1 = int(input("Enter a whole number "))
num2 = int(input("Enter another whole number"))
print("press 1 for +")
print("press 2 for -")
print("press 3 for x")
print("press 4 for /")
operation = int(input("Chose an operation from above"))

def add(num1,num2):
   return num1+num2
def minus(num1,num2):
   return num1-num2
def product(num1,num2):
   return num1*num2
def div(num1,num2):
   return num1/num2

if operation == 1:
    print("The sum of the 2 numbers is:" ,add(num1,num2))

elif operation == 2:
    print("The difference of the 2 numbers is:", minus(num1,num2))

elif operation == 3:
    print("The product of the 2 numbers is:" ,product(num1,num2))

elif operation == 4:
    print("The division of the 2 numbers is:" ,div(num1,num2))
else:
    print("Not a valid number.")



