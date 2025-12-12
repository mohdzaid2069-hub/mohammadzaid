num=int(input("Enter your number to print factors :"))
for i in range(1, (num//2)+1):
    if num%i==0:
        print(i,end=" ")