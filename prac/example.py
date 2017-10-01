#!/usr/local/bin/python

#------------

print('Hello World')

print("Double quotes")

print('concatena'+'tion')

print('hello','there')

#print(5+'I am'+5)

print('I\'m 5')

print("I'm 5")

print('He said "hi"')

word = "Hello World"

print word[:3]

#-----------

exVar = 100
print(exVar)

opVar = exVar / 5.3
print(opVar)

_100ma=5
print(_100ma)
print (" ")

#------------- WHILE
'''
asaas
asasa
'''

#for finite tasks, very structured amount

condition = 1
while condition <= 10:
	print (condition)
	condition += 1

condition = 5
while condition < 15:
	print('True')
	break

#------------- FOR

# that  has variable time frames, don't know time frame
# can be interchanged with while, preferably for is good

exampleList = [1,6,5,7,9,0]

for thing in exampleList:
	print(thing)
	print("")

for x in range(1,11):
	print (x)

#------------- IF

x = 2
y=7
z= 10

if x > y:
	print(x,'is greater than',y)

if x < y:
	print(x,'is less than',y)

if x==y:
	print(x,'is the same as',y)

#cannot do this
#if x < '2':
#	print(x,'is less than 2')

if x <= y:
	print (x, ' is less than or equal to', y)

if z > y > x < z > y:
	print (z, 'is greater than ', y,' which is greater than',x)

#--------------- IF ELSE

x =13
y=6

if x < y:
	print(x,'is less than ',y)
if x > y:
	print(x,'is greater than ',y)
else:
	print(x,'is not less than', y)

#---------- IF ELIF

x =9
y=7
z=10

if x < y or x > y and z > y:
	print('something worked here')
elif y > z:
	print(x,'is greater than ',y)
elif z > y:
	print(z, 'is greater than',y)
else:
	print('nothing is the case')

#------------