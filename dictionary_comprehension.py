# Python code to demonstrate dictionary comprehension
# {key: value for (key, value) in iterable}

# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5] 

# but this line shows dict comprehension here 
myDict = { key:value for (key,value) in zip(keys, values)} 
print(myDict)
# We can use below too
myDict = dict(zip(keys, values)) 
print (myDict)


dic = dict.fromkeys(range(5), True)
print(dic)
