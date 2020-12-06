year=int(input("enter any year"))
if year%4==0 and year%400==0:
    print("leap year hai")
elif year%100==0:
        print("leap year hai")
else:
    print("leap year nahi hai")
