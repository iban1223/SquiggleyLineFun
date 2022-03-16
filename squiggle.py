import random
#Python file for writing post script code that will make squiggly lines instead of straight ones

#Function for drawing the squiggly line
#usage squiggle(starting xCoord, starting yCoord, ending xCoord, ending yCoord, amount of points between start and end, file name)
def squiggle(xS, yS, xE, yE, n, fileName):
	file = open(fileName, "a")
	#Setting up variables for making the line
	xIncrement = (xE-xS)/n #Number the x coord will be incremented by each iteration
	yIncrement = (yE-yS)/n #Number the y coord will be incremented by each iteration
	xRand = random.uniform(0,(2*xIncrement)) #X random number for making squigle
	yRand = random.uniform(0,(2*yIncrement)) #Y random number for making squigle
	xNew = xS #New x coord
	yNew = yS #New y coord
	#Starting the drawing of a newpath
	file.write("\nnewpath\n")
	file.write(str(xNew) + " " + str(yNew) + " moveto\n") #Moving to start point
	xNew = xS+xIncrement+xRand
	yNew = yS+yIncrement+yRand
	#Looping to create the line
	for i in range(n):
		#Writing to next point
		file.write(str(xNew+xRand) + " " + str(yNew+yRand) + " lineto\n")
		#Generating coords for next point
		xRand = random.uniform(-1,1)
		xNew = xNew+xIncrement
		yRand = random.uniform(-1,1)
		yNew = yNew+yIncrement
	#Closing the line and the file
	file.write("stroke\n")
	file.close()



class squiggle():
	fileName = "test.eps"
	file = open(fileName, "w")

	file.write("%!PS-Adobe-3.0 EPSF-3.0\n%%BoundingBox: 0 0 300 300\n\n1 setlinejoin\n1 setlinecap\n")
	file.close()

	y = 0
	r = random.randint(0,100)/100
	g = random.randint(0,100)/100
	b = 0


	for i in range(150):
		file = open(fileName, "a")
		file.write(str(0) + " " + str(0) + " " + str(b) + " setrgbcolor\n")
		file.close()
		r = random.randint(0,100)/100
		g = random.randint(0,100)/100
		b += (2/3)/100
		squiggle(0,y,300,y, 500, fileName)
		y += 2

	file = open (fileName, "a")

	file.write("\nshowpage\n%EOF")
	file.close()