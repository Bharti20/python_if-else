month_num=int(input("enter the month number"))
if month_num==1 or month_num==3 or month_num==8 or month_num==10 or month_num==12 or month_num==5 or month_num==7:
    print("31 dyas")
elif month_num==2:
    print("29 days")
else:
    print("30 dyas")