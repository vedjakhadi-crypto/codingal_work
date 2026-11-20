print("Welcome to the binary conversion program")
num = int(input("Enter a whole number."))

if num > 255 :
    print("Number invalid, try a number lower than 255")

while num >= 1:
    if num%2 > 0:
        print("1")
    else:
        print("0")
    num = int(num/2)
    