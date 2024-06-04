# the enumerate() function is used to iterate over a sequence, such as a list, and it returns both the index and the item at that index. The enumerate() function takes an optional start parameter, which specifies the value from which the index should start.
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print(obj2) #enumerate object
print (list(obj1)) 

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))


l1 = ["eat", "sleep", "repeat"]
print(list(enumerate(l1)))
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)
 
# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print (count, ele) #enumerate returns a tuple (count, ele)
 
# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)

#Accessing the Next Element
fruits = ['apple', 'banana', 'cherry']
enum_fruits = enumerate(fruits)

print(f"Current Element: {enum_fruits}")
next_element = next(enum_fruits)
print(f"Next Element: {next_element}")



next_element = next(enum_fruits)
print(f"Next Element: {next_element}")

