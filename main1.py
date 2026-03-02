numbers=[]
for i in range(5):
    num=int(input("Enter number:"))
    numbers.append(num)
total=sum(numbers)
average=total/len(numbers)
print(numbers)
print(total)
print(average)