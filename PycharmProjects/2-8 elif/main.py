'''
g = int (input("enter score"))
if (g >= 90):
    print("A")
else:
    if (g>=80):
        print("B")
    else:
        if (g>=70):
            print("C")
        else:
            if (g>=60):
                print("D")
            else:
                print("F")
'''
g = int (input("enter score"))
if (g >= 90):
    print("A")
elif (g>=80):
        print("B")
elif(g>=70):
            print("C")
elif (g>=60):
        print("D")

else:print("F")