salary=int(input("enter the salary"))
year=int(input("enter the year"))
if year>5:
    print(salary + ((5*salary)//100))
elif year<5:
    print("it is your salary without bonus",salary)
