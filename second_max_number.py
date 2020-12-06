a = 1
b = 16
c = 100
if a>b and a>c:
    print("first max",a)
elif b>a and b>c:
    print("first max",b)
elif c>a and c>b:
    print("first max",c)
if b>c and b<a:
    print("second max",b)
elif c>b and c<a:
    print("second max",c)
elif a>c and a<b:
    print("second max",a)
elif c>b and c<b:
    print("second max",c)
elif a>b and a<c:
    print("second max",a)
elif b>a and b<c:
    print("second max",b)
else:
    ("invalid")