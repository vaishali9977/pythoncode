n1=int(input("Enter  first number"))
n2=int(input("Enter secind number"))
sum=(n1+n2)
c=0
print("The sum of given number is : ",sum)
if sum%2==0:
    print("Even number:",sum)
else:
    print("Odd number:",sum)
while sum>0:
    for i in range(1,sum+1):
         r=int(sum%i)
         #print(r)
         if r==0:
             c=c+1
print(c)   
if c==2:
    print("prime no",sum)
else:
    print("not prime",sum)

