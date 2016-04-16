import math

def rounding(number):
	if number - math.floor(number) < .5:
		return math.floor(number)
	elif number - math.floor(number) >= .5:
		return math.floor(number) + 1
	

def degToMinSec(degree):
	deg = math.floor(degree)
	min = math.floor((degree - deg) * 60)
	sec = rounding((((degree - deg) * 60) - min) * 60)
	return str(int(deg)) + "DEG " + str(int(min)) + "'" + str(int(sec)) + "''"
	
print degToMinSec(47.323243)

def minSecToDeg (degree, minute, second):
	if minute > 60:
		return 'error: minutes greater than 60'
	elif second > 60:
		return 'error: seconds greater than 60' 
	degree += minute / 60.0 + second / 3600.0
	return degree
	
print minSecToDeg(12, 17, 45)