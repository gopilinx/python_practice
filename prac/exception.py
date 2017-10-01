#!/usr/local/bin/python
try:
	#print('Running the try')
	#print('5'+5)
	#print('5'+x)
	#import mars
	#input('what is your name? ')
	#print(str(name))
	print(x)

#print('code continues....')

except TypeError as t:
	print('Type error triggered')
	print(str(t))

except NameError as n:
	print('Name error triggered')
	print(str(n))

except Exception as e:
	print('General Exception')
	print(str(e))