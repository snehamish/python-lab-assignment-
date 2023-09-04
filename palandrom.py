num2=int(input("enter the five digit number:"))

a=num2//10000
num=num2%10000
b=num//1000
num=num%1000
c=num//100
num=num%100
d=num//10
e=num%10

e=e*10000
d=d*1000
c=c*100
b=b*10

num1=a+b+c+d+e
print(num2)
print(num1)
if num2==num1:
    print("it is a palandrome number" )
else:
    print("it is not a palandrome number" )


