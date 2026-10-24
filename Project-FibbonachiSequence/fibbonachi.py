print("Welcome to the fibbonachi sequence.")

length = int(input("Enter which position to stop at."))
a = 0
b = 1
i = 0
for i in range(length):
    print(a)
    a,b = b,a+b
    i+=1
    