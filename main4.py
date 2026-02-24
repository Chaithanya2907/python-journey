product_price=int(input("Enter the product price:"))
cust_type=input("Enter the customer type:")
if cust_type=="student":
    print("student")
    percenatge=20 
else:
    print("regular")
    percentage=10% discount

discount=(percenatge *product_price)/100
final=product_price-discount

print(f"Original price:{product_price}")
print(f"Discount amount:{discount}")
print(f"Final price:{final}")
    