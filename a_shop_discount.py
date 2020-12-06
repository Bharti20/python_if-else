pur_quantity=int(input("enter the quantity"))
if pur_quantity>1000:
    print(pur_quantity - ((10*pur_quantity)//100))
else:
    print("no discount")