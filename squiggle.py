#Python file for writing post script code that will make squiggly lines instead of straight ones

#Function for drawing the squiggly line
def squiggle(xS, yS, xE, yE, n, fileName):
	file = open(fileName, "a")
	xIncrement = (xE-xS)/n
	yIncrement = (yE-yS)/n
	xNew = xS
	yNew = yS
	file.write("\n")
	file.write("newpath\n")
	file.write(str(xNew) + " " + str(yNew) + " moveto\n")
	xNew = xS+xIncrement
	yNew = yS+yIncrement
	for i in range(n):
		file.write(str(xNew) + " " + str(yNew) + " lineto\n")
		xNew = xNew+xIncrement
		yNew = yNew+yIncrement
	file.write("closepath\nstroke\nshowpage\n")
	file.close()



class squiggle():
	fileName = "test.eps"
	file = open(fileName, "w")

	file.write("%!PS-Adobe-3.0 EPSF-3.0\n%%BoundingBox: 0 0 300 300\n\n1 setlinejoin\n1 setlinecap\n")
	file.close()

	squiggle(0,0,150,150, 300, fileName)

	file = open (fileName, "a")

	file.write("\n%EOF")
	file.close()