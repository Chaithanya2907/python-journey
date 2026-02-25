 
for attempt in range(3):
    password=int(input("Enter password:"))
    if password==1234:
        print("Access granted")
        break
    else:
        print("Wrong passord")
else:
    print("System locked")
        
    
    