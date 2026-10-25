print("Welcome to the prime number identification program.")

num1 = int(input("Enter a whole number that you want to start the set with. "))
num2 = int(input("Enter a whole number that you want to end the set with. "))


fl=0
for i in range (num1,num2+1):
    if i > 1:
        for j in range(2,i):
            if (i%j==0):
                fl=0
                break
            fl=1
        if fl == 1:
            print("This is a prime number: ", i)
        
    else:
        print("1 is not a prime number and neither are negative numbers.")
if fl !=1:
    print("No number is prime in your range.")