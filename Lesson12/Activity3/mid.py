print("Welcome to the middle digit program")

num = input("Enter a number with more that 4 place values.")
length = len(num)

mid = length//2

if length % 2 == 0:
    mid1 = int(num[mid-1])
    mid2 =int(num[mid])
    print("The final proguct of the median of the numbers is: ", mid1*mid2)
else:
    print("The final product of the median of the number is: ", num[mid])
