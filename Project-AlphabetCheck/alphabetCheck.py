print("Welcome to the Alphabet Check.")

character = input("Press any key from your keyboard")

if type(character) == float or int:
    print("Your character is not an alphabet.")
elif type(character) == bool:
    print("More than 1 character is not accepted")
else:
    print("Your character is a sybol or an alphabet")