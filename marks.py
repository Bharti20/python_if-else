phy=int(input("enter the marks"))
chem=int(input("enter the marks"))
bio=int(input("enter the marks"))
math=int(input("enter the marks"))
comp=int(input("enter the marks"))
percentage=(((phy+chem+bio+math+comp)*100)//500)
if percentage>=90:
    print("A grad")
if percentage>=80:
    print("B grad")
if percentage>=70:
    print("c grad")
if percentage>=60:
    print("D grad")
if percentage>=40:
    print("E grad")
if percentage<=40:
    print("F grad")

