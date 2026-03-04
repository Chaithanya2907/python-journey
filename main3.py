num=8
while True:
    sec=int(input("Enter number:"))
    if sec==num:
        print("Correct!")
    elif sec>=num:
        print("high")
    else:
        print("Low")
