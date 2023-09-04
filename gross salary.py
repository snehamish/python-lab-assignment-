bs=int(input("enter the basic salary:"))
hra=bs*(20/100)
ta=bs*(5/100)
da=bs*(10/100)
gs=bs+hra+da+ta
print("the gross salary is:",gs)
if  gs<=300000:
    print("income tax is 0")
elif gs>300000 and gs<=1000000:
    print("income tax is ",gs*(10/100))
elif gs>1000000 and gs<=2500000:
    print("income tax is ",gs*(20/100))
else:
    print("income tax is ",gs*(30/100))

