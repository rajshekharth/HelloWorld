#Write a function that finds the distance between two points and returns it.
#The distance between two points with x,y, and z components can be calculated
#as:

#distance=sqrt((x2−x1)**2+(y2−y1)**2+(z2−z1)**2) The input for this function \
#will be two 1 Dimensional lists that contain the x,y,z coordinates each.
#For example if the input lists are:
#a = [2, 3, -5] 
#b = [4, -3, 12]
#Then your function should return their distance such as:
#18.138357147217054
#Hint: You may use the math module!

from math import *

def calc_dist(point1,point2):
    x1,y1,z1=point1[0],point1[1],point1[2]
    x2,y2,z2=point2[0],point2[1],point2[2]
    distance = ((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**(1/2)
    return distance

## Main Program ##
print('Enter first coordinates : ')
coordinates1 = [int(x) for x in input().split()]
print('Enter second coordinates : ')
coordinates2 = [int(x) for x in input().split()]
dist=calc_dist(coordinates1,coordinates2)
print('The distance beween two coordinates is',dist)
