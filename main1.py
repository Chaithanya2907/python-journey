name=str(input("Enter an string:"))
count=0
for i in name:
    if i.lower() in "aeiou":
        count=count+1
print(count)