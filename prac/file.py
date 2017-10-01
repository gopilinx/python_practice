#!/usr/local/bin/python

# Writing and Appending to a file -  2 methods
# Writing - overwritten - picture is example

writeMe = 'Example text '

saveFile = open('examplewrite.tx','w')
saveFile.write(writeMe)
saveFile.close()

# Append - going to add 

appendMe = 'some text '

saveFile = open('exampleappend.txt', 'a')
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()

# Reading from a file

readMe = open('exampleappend.txt','r').read()
print(readMe)

splitMe = readMe.split('\n')
# Read from a python list
print(splitMe[4])

readMe2 = open('exampleappend.txt','r').readlines()
print(readMe2)