num=int(input("enter the three digit number:"))
a=num//100
num=num%100
b=num//10
c=num%10
sum1=a**3+b**3+c**3
if sum1==num:
    print(sum1,"it is an armstrong number")
else:
    print(sum1,"it is armstrong number")

