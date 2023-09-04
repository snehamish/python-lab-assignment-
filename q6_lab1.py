a=int(input("Enter coffi. of X square :"))
b=int(input("Enter coffi. of X :"))
c=int(input("Enter constant :"))

d=((b**2)-(4*a*c))
root1=((-b)+(d**0.5))/2*a
root2=((-b)-(d**0.5))/2*a

print("Roots of the quad. equation are : ",root1, root2)