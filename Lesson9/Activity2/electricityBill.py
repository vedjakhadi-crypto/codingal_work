print("Welcome to the electricity bill app")

electricityUnit = str("How much electricity units have you consumed?")
bill = 1

if electricityUnit <=50:
    bill = (electricityUnit*2.6) + 25
    print("Your electricity bill is ", bill)
elif electricityUnit >50 and electricityUnit<=100 :
     bill = (electricityUnit*3.25) + 35
     print("You electricity bill is ",bill)
elif electricityUnit >100 and electricityUnit<=200 :
     bill = (electricityUnit*5.26) + 45
     print("You electricity bill is ",bill)
elif electricityUnit >200:
    bill = (electricityUnit*8.45) + 75