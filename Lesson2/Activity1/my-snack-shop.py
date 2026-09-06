snack_name = "chips"
price = 1.50
quantity = 100
is_available = True
print('snack name=', snack_name)
print('price=' , price)
print('quantity=' , quantity)
print('is available' , is_available)
stockvalue = price*quantity
print('total stockvalue=' , stockvalue)
print('stock x 2=' , quantity*2)
if price < 2:
    print("Yes, price is lower than $2.")
if quantity > 5:
    print("Yes,quantity is higher than 5.")
    print("It is affordable")
else : print("It is not worth it.")
