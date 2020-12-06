angle1=int(input("enter the angle's value"))
angle2=int(input("enter the amgle's value"))
angle3=int(input("enter the amgle's value"))
if angle1==angle2 or angle1==angle3:
    print("isosceles tringle")
elif angle1!=angle2!=angle3:
    print("scalene tringle")
elif angle1==angle2==angle3:
    print("equilateral tringle")
else:
    print("invalid")
