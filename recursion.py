import funtion as f

f.factorial(5)

#print number
def print_num(n):
    if(n==0):
        print()
        return 
    
    print(n , end=" ")
    print_num(n-1)
    
print_num(5)

#cal factorial
def factorial(n):
    if(n==1 or n==0):
        return 1
    
    return n*factorial(n-1)

print(factorial(5))

# sum of first n natural numbers
def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)    
print(sum(10))

#print all elements of list

def print_ele(li,idx):
    if(idx==len(li)):
        return
    print(li[idx],end=" ")
    print_ele(li,idx+1)
    
list = [1,2,3,14, 8, 9]
print_ele(list,0)
