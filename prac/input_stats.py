#!/usr/local/bin/python

#Input 

name = input('what is your name?: ')
print('Hello',name)
5
#statistics
import statistics

exList = [5,3,2,9,9,7,4,3,1,8,9]

x = statistics.mean(exList)
print (x)

x = statistics.median(exList)
print (x)

x = statistics.mode(exList)
print (x)

x = statistics.stdev(exList)
print (x)

print(statistics.variance(exList))


# other forms of import


import statistics as s
exList =  [5,2,3,1,2,3]

print(s.mean(exList))

from statistics import mean
print (mean(exList))

from statistics import mean as m
print (m(exList))

from statistics import mean as m, stdev as s
print (m(exList))
print (s(exList))

from statistics import * 
print (mean(exList))
print (stdev(exList))
