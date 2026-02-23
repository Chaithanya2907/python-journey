import math
r=float(input("Enter radius:"))
area=math.pi*r*r

if area>=500:
    ground_type="VIP Ground"
    ticket_price=500
else:
    ground_type="Normal Ground"
    ticket_price=200
print(f"Area:{area}")

 
income=area*ticket_price
print(f"Ticket price:{ticket_price}")
print(f"Total income:{income}")
    
