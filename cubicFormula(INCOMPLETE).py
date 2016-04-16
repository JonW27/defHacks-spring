import math

def cubicFormula(a, b, c, d):
	expression1 = (((-1.0 * (b ** 3.0))/(27.0 * (a ** 3.0))) + ((b * c)/(6.0 * a ** 2.0)) - (d / (2.0 * a)))
	expression2 = ((c / (3.0 * a)) - ((b ** 2.0) / (9.0 * a ** 2.0)))
	expression3 = b / (3.0 * a)
	cubeRoot1 = abs(expression1 + ((expression1) ** 2.0 + (expression2) ** 3.0) ** (1.0/2.0)) ** (1.0/3.0)
	cubeRoot2 = abs(expression1 - ((expression1) ** 2.0 + (expression2) ** 3.0) ** (1.0/2.0)) ** (1.0/3.0)
	if (expression1 + ((expression2) ** 2.0 + (expression3) ** 3.0) ** (1.0/2.0)) < 0:
		return cubeRoot1 * -1
	if (expression1 - ((expression2) ** 2.0 + (expression3) ** 3.0) ** (1.0/2.0)) < 0:
		return cubeRoot2 * -1
	root = cubeRoot1 + cubeRoot2 - expression3
	return root
	
print cubicFormula(1,2,3,8)