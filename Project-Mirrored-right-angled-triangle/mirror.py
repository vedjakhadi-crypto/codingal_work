print("Welcome to the mirrored triangle program")

num = int(input("Enter a whole number "))

for i in range(num):
    j = 0
    for j in range(i+1):
        print("*", end="")
    print()

i = num-1

while i >= 0:
    j = 0
    for j in range(i):
        print("*", end="")
    i-=1
    print()