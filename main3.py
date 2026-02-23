import math
r = float(input("Enter radius:"))
area = math.pi*r*r
price = area*2
if area>200:
    print("Large Pizza!")
else:
    print("Small Pizza!")
print(f"Area:{round(area,2)}")
 
print(f"Price:{round(price,2)}")