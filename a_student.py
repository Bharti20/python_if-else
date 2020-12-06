classes_held=int(input("enter the number of classes held"))
classes_attended=int(input("enter the number of classes attend"))
percentage=int((classes_attended/classes_held)*100)
if classes_attended>75:
    print("allowed to sit in exam",percentage)
elif classes_attended<75:
    print("not allow to sit in exam")




