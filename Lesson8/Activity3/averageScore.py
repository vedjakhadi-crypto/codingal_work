print("welcome to the finding the average marks program.")

science= int(input("Enter your percetage for science "))
geogrphy= int(input("Enter your percentage for geography "))
history= int(input("Enter your percentage for history "))
english= int(input("Enter your percentage for english "))
maths= int(input("Enter your percentage for maths "))

average = float(science + geogrphy + history + english + maths) / 5
print("Your average percentage is " ,average)

if average in range(90,100):
    print("You are the topper")
elif average not in range(90,100) and average in range(80,89):
    print("Very good score")
else:
    print("Better luck next time")