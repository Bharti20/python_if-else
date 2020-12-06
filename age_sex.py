age=int(input("enter the age"))
sex=(input("enter the sex"))
maretial_status=input("enter the status")
if sex=="female":
    if maretial_status=="yes" or maretial_status=="no":
        print("she will work only urban area")
elif sex=="male":
    if age>=20 and age<=40:
        if maretial_status=="yes" or maretial_status=="no":
           print("he can work anywhere")
    elif age>=40 and age<=60:
        if maretial_status=="yes" or maretial_status=="no":
            print("he will work in urban areas")
    else:
        print("error")



