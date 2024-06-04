#enum is short for "enumeration" and refers to the Enum class in Python's enum module.
from enum import Enum,unique

# class subjects(Enum):
#    ENGLISH = 1
#    MATHS = 2
#    SCIENCE = 3
#    SANSKRIT = 4

# obj = subjects.MATHS
# print (type(obj), obj.value)

# obj_2 = subjects.SCIENCE
# print (obj_2.name, obj_2.value )

# class subjects(Enum):
#    ENGLISH = "E"
#    MATHS = "M"
#    GEOGRAPHY = "G"
#    SANSKRIT = "S"
   
# obj = subjects.SANSKRIT
# print (type(obj), obj.name, obj.value)

# 

print()

# @unique
# class subjects(Enum):
#    ENGLISH = 1
#    MATHS = 2
#    GEOGRAPHY = 3
#    SANSKRIT = 2

subject = Enum("subjects", "ENGLISH='E', MATHS='M', SCIENCE='S, SANSKRIT='s")
print(type(subject))
for sub in subject:
   print (sub.name, sub.value)
