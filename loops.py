# program to find sum of n natural number
import datetime

x = datetime.datetime.now()
print(x)

sum, i = 0, 1
n = int(input("enter num: "))
while i<=n:
    sum += i
    i+=1
    
print(sum)

# for i in range(0,n+1):
#     sum+=n
    

# factorial of a number
n = int(input("enter your num: "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
    
print(fact)