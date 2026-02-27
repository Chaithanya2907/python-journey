password= " "
password=input("Enter Password:")
has_upper=False
has_lower=False
has_digit=False
for i in password:
    if i.isupper():
        has_upper=True
    if i.islower():
        has_lower=True
    if i.isdigit():
        has_digit=True
if len(password)>=8 and has_upper and has_lower and has_digit:
    print("Strong password")
else:
    print("Weak password")     
    
    
