#python program to check given number is prime or not
n=int(input("Enter an integer number"))
k=0
for i in range(1,n+1):
    rem=n%i
    if rem==0:
        k=k+1
if k==2:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")

print("End of the program")    
