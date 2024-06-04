import platform
# from function import factorial(n)
#Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]

x = platform.system()
print(x)
x = dir(platform)
print(x)
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:


import os
# f = open("funtion.py", "r")

# data = f.read()
# print(type(data))

# f.close()

# f = open("python_basics.py", "w")
# data = f.write("#hello world")

with open("python_basics.py", "a+") as f:
    f.write(" shaili")

os.remove("python_basics.py")

with open("practice.txt", "w") as f:
    f.write(" Hi, everyone!\n we are learning file io\n using java,\n I love java programming.. ")
    
with open("practice.txt", "r") as f:
    str = f.read() # this return a string value
    print(str)
    str = str.replace("java", "python")
    print(str)

def find_word(file, word):

    with open(file) as f:
        str = f.read()
        if(str.find(word) != -1):
            print(word, "found")
            return 
        print("not found")

find_word("practice.txt", "learning")
        
with open("practice.txt", "r") as f:
    str = f.read()
    #for index of learning
    print(str.find("learning"))
    
# find word in which line
def find_word_line(file, word):
    with open(file,"r") as f:
        line = True
        i = 1
        while (line):           
            line = f.readline()
            if (word in line):
                return i
            i+=1
    
        return -1
 
print(find_word_line("practice.txt", "programming"))

# os.remove("practice.txt")
with open("practice.txt", "w+") as f:
    f.write("1,3,56,97,84,20,2") # this moves cursor to end of file
    f.seek(0) # we again starting cursor from beginning
    str = f.read()
    # print(str)
    num = ""
    for i in range(0, len(str)):
        # this will skip last num
        if(str[i]==","):
            print(num)
            num = ""
        else:
            num = num+str[i]



with open("practice.txt", "r") as f:
    data = f.read()
    num = data.split(",")
    print(num) # num is list of string items
    count = 0
    for i in num:
        if(int(i)%2==0):
            count+=1

    print("even number : ", count)    

