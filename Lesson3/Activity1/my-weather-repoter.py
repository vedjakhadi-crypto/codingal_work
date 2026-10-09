import datetime
import calendar

print("Welcome to the weather app")
destination=str(input("Where do you live?"))
temprature=float(input("What is the temprature over there?"))


if temprature>30:
    print("It is very hot there.")

if temprature<10:
    print("It's very cold")
else:
    print("Very hot.")


if temprature<10:
    print("It's very cold")
elif temprature==10:
    print("Preety cold")
elif temprature>=15:
    print("Very normal")
else:
    print("Very hot")

print(datetime.datetime.now())
print(calendar.calendar(datetime.datetime.now().year))