ans=int(input("enter the system you would like to use 1.metric, 2.inches and pounds:"))
w=float(input("enter the weight:"))
h=float(input("enter the height:"))
if w<=0 or h<=0 or ans==0 or ans>2:
    print("invaild input")
else:
    if ans==1:
        bmi=w/(h**2)
    else:
        bmi=703*w/(h**2)
    print(bmi)
