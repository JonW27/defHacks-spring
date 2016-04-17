def areaShape(coordinates):
	if len(coordinates) < 3:
		return 'Error: Not A valid 2D shape'
	rightSum = 0
	xpos = 0
	ypos = 1
	while ypos < len(coordinates):
		rightSum += (coordinates[xpos])[0] * (coordinates[ypos])[1]
		xpos += 1
		ypos += 1
	leftSum = 0
	xpos = 1
	ypos = 0
	while xpos < len(coordinates):
		leftSum += (coordinates[ypos])[1] * (coordinates[xpos])[0]
		xpos += 1
		ypos += 1
	areaShape = abs(rightSum - leftSum) / 2
	return areaShape
	
print areaShape([[2,4],[3,-8],[1,2],[2,4]])