#!/usr/local/bin/python

from statistics import mean as m
admins = {'User1':'abc123', 'User2':'xyz123'}

studentDict = {'jeff':[10,20,30,40], 
			   'peter':[80,20,47,20],
			   'sam':[75,34,23,67]}

def enterGrades():
	nameToEnter = input('Enter Student Name: ')
	gradeToEnter = input('Enter Grade: ')
	if nameToEnter in studentDict:
		print('Adding grade....')
		studentDict[nameToEnter].append(float(gradeToEnter))
	else:
		print('Name enter is invalid ')

	print(studentDict)

def removeStudent():
	nameToDelete = input('Enter Student Name to delete: ')
	if nameToDelete in studentDict:
		print('Deleting ', nameToDelete)
		del studentDict[nameToDelete]
	else:
		print('Student to delete doesnt exist ')

	print(studentDict)

def avgGrades():
	for eachStudent in studentDict:
		gradeList = studentDict[eachStudent]
		avgGrade = m(gradeList)
		print(eachStudent, 'Avg Grade is ... ', avgGrade)

def main():
	print ("""
		Welcome to grade school

		[1] - Enter Grades
		[2] - Remove Student
		[3] - Student Average Grades
		[4] - Exit
		""")
	action = input('What you wanted to do? ')
	if action == '1':
		enterGrades()
	elif action == '2':
		removeStudent()
	elif action == '3':
		avgGrades()
	elif action == '4':
		exit()
	else:
		print('No valid choice was given')

userName = input('Enter user name ')
userPass = input('Enter user pass ')
	
if userName in admins:
	if userPass == admins[userName]:
		print( "Successfully logged in ", userName)
		while True:
			main()
	else:
		print( "Password wrong exiting")
else:
	print( "user name doesn't exist")
