numbers=[]
even_count=0
odd_count=0
for i in range(10):
    num=int(input("Enter number:"))
    numbers.append(num)
    
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print(even_count)
print(odd_count)
print(numbers)
