#!/usr/local/bin/python

# Dataypes useful in python , lot of like a DB< like  a
# assosiative array, mainly has keys and values
# Unordered groups, key to the value is the only association
# Not like list, tuples ordered
# Keys need to be unique
# Also mutable like list but not ordered

# Notify dictinoaries using { }
gradeDict = {'kelly':89, 'David':65, 'Jack':95, 'Samantha':78}

print(gradeDict)
print(gradeDict['David'])

gradeDict['David'] = 56
print(gradeDict)

gradeDict['Jessy'] = 92
print(gradeDict)

del gradeDict['David']
print(gradeDict)

gradeDict = {'kelly':[89,88],
			 'David':[65,56], 
			 'Jack':[95,78], 
			 'Samantha':[66,78]}

print(gradeDict)
print(gradeDict['David'])
print(gradeDict['David'][1])