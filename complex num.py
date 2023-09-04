num1=int(input("enter the real part of complex number 1:"))
com1=int(input("enter the imagnare part of the complex number1:"))
num2=int(input("enter the real part of complex number 2:"))
com2=int(input("enter the imagnary part of the complex number:"))      
sum1=num1+num2
sum2=com1+com2
print("the sum is:",sum1,"+i",sum2)
mult1=((sum1*sum2)-(com1*com2))
mult2=((sum1*com2)-(sum2*com1))
print("the multiplication is: ",mult1,"+i",mult2)

