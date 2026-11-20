print("Welcome to the armstrong number program")

num = int(input("Enter a number "))

arm = 0
it = num

while it > 0:
    last = num % 10
    arm = arm+(last**3)
    it = it//10
if arm == num:
    print("It's an armstrong number.")
else:
    print("It's not an armstrong number.")