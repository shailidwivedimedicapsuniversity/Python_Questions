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

# initializing lists
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = zip(name, roll_no, marks)

# converting values to print as list
mapped = list(mapped)

# printing resultant values
print("The zipped result is : ", end="")
print(mapped)

print("\n")

# unzipping values

namz, roll_noz, marksz = zip(*mapped)

print("The unzipped result: \n", end="")
print(zip(*mapped))
# printing initial lists
print("The name list is : ", end="")
print(namz)

print("The roll_no list is : ", end="")
print(roll_noz)

print("The marks list is : ", end="")
print(marksz)


# Python code to demonstrate the application of
# zip()

# initializing list of players.
players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]

# initializing their scores
scores = [100, 15, 17, 28, 43]
print(zip(players, scores))
# printing players and scores.
for pl, sc in zip(players, scores):
	print("Player : %s	 Score : %d" % (pl, sc)) 
	# here using string formatting %s is replaced with the player's name, and the %d is replaced with their score

