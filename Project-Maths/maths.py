print("welcome to the power number program!")

num = int(input("Enter a whole number "))
power = int(input("Enter the power you want your number to be "))

i = 1
n = 1
for i in range(power):
    n*=num
    i+=1
print(n)