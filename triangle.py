x=float(input("enter the first side:"))
y=float(input("enter the second side:"))
z=float(input("enter the third side:"))
if x<=0 or y<=0 or z<=0:
    print("invaild input")
else:
    if x+y>=z or x+z>=0 or y+z>=-0:
        print("it is a triangle")
    else:
        print("it is not a triagle.")
        
