x=float(input("enter the first side:"))
y=float(input("enter the second side:"))
h=float(input("enter the height:"))
if x<=0 or y<=0 or h<=0:
    print("invaild input")
else:
    area=0.5*(x+y)*h
    print(area)
