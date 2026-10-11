print("Welcome to exam eligibility check app.")


attendence = int(input("What is your attendence out of 100"))
print("Y for yes and N for no for the following question.")
medicalConditions = str(input("Do you have any mediccal conditions with proof?"))

if attendence > 75:
    if medicalConditions == "Y":
        print("Sorry! You are not eligible.")
    else:
        print("You are eligible")
else:
    print("You are not eligible.")