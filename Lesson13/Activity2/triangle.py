print("Welcome to the trianglr program")

num = int(input("Enter a whole number"))

for i in range(num):
    for j in range(i+1):
        print("*", end="")
    print()