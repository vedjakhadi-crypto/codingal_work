print("Welcome to the trianglr program")

num = int(input("Enter a whole number "))

a = 1

for i in range(num):
    for j in range(i+1):
        print(a, end=" ")
        a+=1
    print()
# print("hi")
# print("hi", end="Ved")
# print("hi")
# print("hi")