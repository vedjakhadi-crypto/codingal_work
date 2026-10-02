passengername=input("What is your name? ")
destination=input("Where do you want to go? ")
price=7.00
numberoftickets=int(input("How much tickets do you need? "))
ticketavailablity=True
print(type(passengername))
print(type(destination))
print(type(numberoftickets))
print(type(price))
print(type(ticketavailablity))
total_cost = price*numberoftickets
print("total cost is: ",total_cost)
discountedprice=price*numberoftickets*0.10
print("discounted price is: ",discountedprice)
finalprice=price*numberoftickets-discountedprice
print("final price is: ",finalprice)
increasedprice=price*numberoftickets+2
print("Increased price is: ",increasedprice)
halfprice=price*numberoftickets/2
print("Half price is: ",halfprice)
limit=10
if price<limit:
    print("Ticketprice is lower than the limit.")
if 2<numberoftickets:
    print("You have booked more than 2 tickets.")
if destination=="Goa":
    print("Your tickets for Goa are booked.")
if price<20:
    print("Hope we see you again.")
print("Have a safe journey to"+" "+destination+" "+"Hope your holiday goes well.")
print(destination.upper())
print(passengername.lower())
print(destination.index[2])
print(passengername.len())