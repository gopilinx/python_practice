#!/usr/local/bin/python

def example1():
	x =1
	y = 3
	print(x+y)

	if x < y:
		print (x, 'is less than', y)

#def main():
	#example()

#main()

#----------- Funtions Params

def addition(num1,num2,num3,num4):
	answer = num1+num2+num3+num4
	return answer

#def main():
#	x=addition(2,3,4,3)
#	print(x)

#main()


# Recommendation is if more than 2 set some defaults
def website(font='TNR',
			background_color='white',
			font_size='11',
			font_color='black'):
	print('font:',font)
	print('bg:',background_color)
	print('Font Size:',font_size)
	print('Font color:',font_color)

#website(background_color="black",font="TNR",
#		font_color="black",
#		font_size='11')

#website(background_color='grey')
#website('ABC','yellow')


#---------- Global and Local variables

x = 6

#not recommended to use global call and modify
def example3():
	global x
	x += 1
	print (x)

def example():
	z = 5
	print(z)

#cannot do this
#print(z)

def example2():
	z =7
	print(z)
	print(x)
	#this we can't do
	#x += 1
	y = x + 2
	#print(y)
	return y

def main():
	x=example2()
	print(x)

main()






