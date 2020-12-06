amount=int(input("enter any amount"))
note=int(input("enter the note"))
if note==100:
    print(amount//100)
elif note==50:
    print(amount//50)
elif note==20:
    print(amount//20)
elif note==5:
    print(amount//5)
elif note==200:
    print(amount//200)
elif note==10:
    print(amount//10)
elif note==2000:
    print(amount//2000)
else:
    print("invalid")

