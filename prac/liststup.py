#!/usr/local/bin/python 

# Tuples, list
# Similar, dif Tuples - inmmutable not changed once defined
# Use tuples - specific reason for inmmutable
# List is mutable and can be changed

# Tuples  - used for variable assignments, sequence and unpackings
# either in round bracket or as lilst
# takes up less space and faster, iterate easily as oppose to list

def example():
	return 15 ,19

a,b = example()

print(a)
print(b)

# Lists - mutable	
# Refers to an array but not arry its a list
# Add, remove, combine, sort, count etc...
# demanipulated

x = [6,2,3,2,5,7,3,7] 

print(x)
print(x[5])

x.append(12)
print(x)

#insert at the specific index
x.insert(5,9)
print(x)

#only remove the first occurence
x.remove(7)
print(x)

#search for index
print(x.index(12))

#count occurences index
print(x.count(9))

x.sort()
print(x)

x = ['sam', 'peter', 'kim', 'jim']
print(x)
x.sort()
print(x)
x.reverse()

