import loops
#Note: When using a function from a module, use : module_name.function_name.
a = loops.n
print(a)
# # avg of 3 number
# def avg(a,b,c):
#     avg = (a+b+c)/3
#     return avg
    
# print(avg(2,3,4))

# # factorial
# n = int(input("enter your num: "))

# def calc_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact*i
        
#     print(fact)

# calc_fact(n)
    
# # calc percetage
# def cal_percent(marks):
#     sum = 0
#     for i in range(0, len(marks)):
#         sum += marks[i]
        
#     percent = sum/len(marks)
#     return percent


# marks = [100, 98,99,90]
# print("your percentage is : " + str(cal_percent(marks)))

# #print list item
# def cal_len(li):
#     for i in li:
#         print(i, end = " ")
    
# list = [3,5,6,6,7,9,9,9,9,10,11,12]
# # print(cal_len(list))
# cal_len(list) 

#cal factorial
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    print(fact)
    
factorial(5)

#dollar to rupees
def usd_to_rupee(usd):
    return usd*83
    
print(usd_to_rupee(100))