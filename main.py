a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if a>b and a>c:
    print("largest is:",a)
elif b>a and b>c:
    print("largest is:",b)
else:
    print("largest is:",c)
if a<b and a<c:
    print("lowest is:",a)
elif b<a and b<c:
    print("lowest is:",b)
else:
    print("lowest is :",c)
