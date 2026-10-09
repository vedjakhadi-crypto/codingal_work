wieght = float(input("What is your wieght?"))
hieght = float(input("What is your hieght in inches?"))
bmi = wieght/((hieght/100))**2
if bmi >= 18.4:
    print("You are underwieght.")
elif bmi >= 24.9:
    print("You are fit")
elif bmi >= 29.9:
    print("You are overwieght")
elif bmi >= 39.9:
    print("You are obesse")
else:
    print("You are severly obesse")