##Python zip() method takes iterable containers and returns a single iterator object, having mapped values from all the containers. 

#join 2 lists/tuples/sets/strings together internally in a tuples of pairs , returns a zip object
list1 = {1,2,3,4,5}
list2 = {'a','b','c'}

zipped  = zip(list1,list2)
print(zipped) 
x = list(zipped)
print(x) #[(1, 'b'), (2, 'c'), (3, 'a')]
newdict = {key:value for key,value in x}
print(newdict)

a = ("John", "Charles", "Mike")
b = ["Jenny", "Christy", "Monica"]

x = zip(a, b)
print(x)
# print(list(x))
print(tuple(x))

names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages)):
	print(i, name, age)
	
stocks = ['GEEKS', 'For', 'geeks']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,
			prices in zip(stocks, prices)}
print(new_dict)


tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped = zip(tuple1, tuple2)
result = list(zipped)
print(result)


list1 = [1, 2, 3]
list2 = {'a', 'b', 'c'}
list3 = ('x', 'y', 'z')
list4 = "shaili"

zipped = zip(list1, list2, list3, list4)
result = list(zipped)
print(result)
