fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#you want a new list, containing only the fruits with the letter "a" in the name.
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#with list cpmprehension newlist = [expression for item in iterable if condition == True]

# newlist = [x for x in fruits if "a" in x] , newlist = [x for x in range(10) if x<10]

newlist = [a.upper() for a in fruits if x!='apple']
print(newlist)

newlist = ['shaili' if x != "banana" else "orange" for x in fruits ]
print(newlist)

newlist = [x for x in fruits if len(x)<4 ]
if(len(newlist)==0):
  print("no such words")
else:
  print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

my_list = [1,3,5,7,9,2,4,6,8]
new_list = [5 if x % 2 == 0 else (7 if x > 5 else x) for x in my_list] # we can't solve this using elif

print(new_list)

print ("shaili") if 1>3 else print("dwivedi")

