from datetime import datetime
DISCOUNT_RATE=.1
TAX_RATE=0.06
today=datetime.today()
if dow==today.weekday():
    if subtotal==0:
        subtotal=float(input("Enter the subtotal: "))
quantity=1
while quantity !=0:
    quantity=int(input("Enter the quantity: "))
if quantity==0:
    print(f'Total: {subtotal}')
discount=0
if dow==2 or dow==3 or dow==4:
    if subtotal >= 50:
        discount=subtotal * DISCOUNT_RATE
        print(f'Discount: {discount}')
    else:
        short=50-subtotal
        print(f'You are ${short} away from a discount')
subtotal -= discount
tax=subtotal * TAX_RATE
total=subtotal + tax

print(f'Tax: {tax}')
print(f'Total Due: {total}')