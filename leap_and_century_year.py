year=int(input("enter the year"))
if year%400==0 and year%100==0:
    if year%4==0:
        print("leap year hai")
elif year%4==0 and year%100!=0:
        print("leap year")
else:
    print("leap year nahi hai")