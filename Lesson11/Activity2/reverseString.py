print("Welcome to reversing a string program.")

name = input("Enter your name. ")
empty = ""
print("Your name is :" ,name)
for i in name:
    empty = i+empty
print("Your name reversed is: " ,empty)