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

# creation using list comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)

sDict = {x.upper(): x*3 for x in 'coding '}
print (sDict)

# comprehension using if.
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)

# given string
l="GFG"

# using nested dictionary comprehension
dic = {
	x: {y: x + y for y in l} for x in l
}

print(dic) # output - {'G': {'G': 'GG', 'F': 'GF'}, 'F': {'G': 'FG', 'F': 'FF'}}

# keys should be unique in dic for that this is not output
# {'G': {'G': 'GG', 'F': 'GF', 'G':'GG'}, 'F': {'G': 'FG', 'F': 'FF', 'G':'FG'}, 'G':{'G': 'GG', 'F':'GF', 'G':'GG'}} 