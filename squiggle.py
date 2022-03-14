import random
#Python file for writing post script code that will make squiggly lines instead of straight ones

#Function for drawing the squiggly line
#usage squiggle(starting xCoord, starting yCoord, ending xCoord, ending yCoord, amount of points between start and end, file name)
def squiggle(xS, yS, xE, yE, n, fileName):
	file = open(fileName, "a")
	#Setting up variables for making the line
	rand = random.randrange(0,2) #Random number for making squigle
	xIncrement = (xE-xS)/n #Number the x coord will be incremented by each iteration
	yIncrement = (yE-yS)/n #Number the y coord will be incremented by each iteration
	xNew = xS #New x coord
	yNew = yS #New y coord
	file.write("\n")
	#Starting the drawing of a newpath
	file.write("newpath\n")
	file.write(str(xNew) + " " + str(yNew) + " moveto\n") #Moving to start point
	xNew = xS+xIncrement+rand
	yNew = yS+yIncrement+rand
	#Looping to create the line
	for i in range(n):
		#Writing to next point
		file.write(str(xNew) + " " + str(yNew) + " lineto\n")
		#Generating coords for next point
		rand = random.randrange(0,2)
		xNew = xNew+xIncrement+rand
		rand = random.randrange(0,2)
		yNew = yNew+yIncrement+rand
	#Closing the line and the file
	file.write("stroke\n")
	file.close()



class squiggle():
	fileName = "test.eps"
	file = open(fileName, "w")

	file.write("%!PS-Adobe-3.0 EPSF-3.0\n%%BoundingBox: 0 0 300 300\n\n1 setlinejoin\n1 setlinecap\n")
	file.close()


	squiggle(0,0,150,150, 500, fileName)

	file = open (fileName, "a")

	file.write("\nshowpage\n%EOF")
	file.close()