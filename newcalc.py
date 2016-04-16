import Tkinter, math #main bits of code go here
from Tkinter import *

class Application(Frame):
    #Keep the functions here, let's use .grid() instead of .grid()
    #DEFINE THE FUNCTIONS HERE
 #   def functionLoad(self):
        #newfile = open(filename, 'rw')
        #read = newfile.read()
    #    filename = self.xinput.get('1.0', 'end-1c')
       # print filename
#        func = self.yinput.get('1.0', 'end-1c')#NEEDS PARAMETERS TO BE ENTERED
   #     e = open(filename, 'rU')
      #  f = e.read()
        #g = f.split("def")[0]
       # print repr(g)
        
    #you can add the built-in functions here.
    def addition(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(x + y)
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def subtraction(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(x - y)
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def multiplication(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(x * y)
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def division(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(x / y)
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)

    def CLS(self):
        self.display.delete('1.0', 'end')
        print("##############")
        print("")
        print("CLEARED")
        print("")
        print("##############")
    def ceiling(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.ceil(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def factorial(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = int(float(x))
        z = float(math.factorial(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def copysign(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(math.copysign(x, y))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def modulus(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(math.fmod(x, y))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def absolute(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.fabs(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def floor(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.floor(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def greatestcd(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(math.gcd(x, y))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def exp_e(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.exp(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def logarithm(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(math.log(x, y))
        print(z)
        z = str(z) 
        z = z + "\n"
        self.display.insert(END, z)
    def logten(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.log10(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def power(self):
        x = self.xinput.get('1.0', 'end-1c')
        y = self.yinput.get('1.0', 'end-1c')
        x = float(x)
        y = float(y)
        z = float(math.pow(x, y))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def sqroot(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.sqrt(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def arccos(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.acos(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def arcsin(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.asin(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def arctan(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.atan(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def cosine(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.cos(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def sine(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.sin(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def tangent(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.tan(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def arccosineh(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.acosh(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def arcsineh(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.asinh(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def arctangenth(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.atanh(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def cosineh(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.cosh(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def sineh(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.sinh(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def tangenth(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.tanh(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def cosecant(self):
	x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.sin(x))
	z = 1 / z
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def secant(self):
	x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.cos(x))
	z = 1 / z
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def cotangent(self):
	x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.tan(x))
	z = 1 / z
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def arccsc(self):
	x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.asin(x))
	z = 1 / z
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def arcsec(self):
	x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.acos(x))
	z = 1 / z
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def arccot(self):
	x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.atan(x))
	z = 1 / z
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def degrees(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.degrees(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def radians(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.radians(x))
        print(z)
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def pi(self):
        z = math.pi
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def e(self):
        z = math.e
        z = str(z)
        z = z + "\n"
        self.display.insert(END, z)
    def carryX(self):
        disp = self.display.get('1.0', 'end-1c')
        disp = str(disp)
        print(disp)
        self.display.delete('1.0', 'end')
        self.xinput.delete('1.0', 'end')
        self.xinput.insert(END, disp)
    def carryY(self):
        disp = self.display.get('1.0', 'end-1c')
        disp = str(disp)
        print(disp)
        self.display.delete('1.0', 'end')
        self.yinput.delete('1.0', 'end')
        self.yinput.insert(END, disp)
    def rand(self):
        rand = random.randint(0, 1000000000)
        print(rand)
        rand = str(rand) + "\n"
        self.display.insert(END, rand)
    def permutations(self):
	n = int(self.xinput.get('1.0', 'end-1c'))
	r = int(self.yinput.get('1.0', 'end-1c'))
        answer = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
        answer = str(answer)
	answer += "\n"
        self.display.insert(END, answer)    
    def combinations(self):
	n = int(self.xinput.get('1.0', 'end-1c'))
	r = int(self.yinput.get('1.0', 'end-1c'))
        answer = math.factorial(n)/math.factorial(n - 3)
	answer = str(answer)
	answer += "\n"
        self.display.insert(END, answer) 
    def geometric(self):
	x = int(self.xinput.get('1.0', 'end-1c'))
        y = int(self.yinput.get('1.0', 'end-1c'))
        answer = x * ((1 - x) ** (y - 1))
	answer = str(answer)
	answer += "\n"
        self.display.insert(END, answer) 
    def binomialcdf(self):
	n = int(self.xinput.get('1.0', 'end-1c'))
	q = int(self.yinput.get('1.0', 'end-1c'))
	x = int(self.zinput.get('1.0', 'end-1c'))
	p = int(self.winput.get('1.0', 'end-1c'))
        answer = ((math.factorial(n)) / ((math.factorial(n - x))(math.factorial(x)))) * (p ** x)(q ** (n - x))
	answer = str(answer)
	answer+= "\n"
        self.display.insert(END, answer) 
    def rot13Chr(self):
	ch = str(self.xinput.get('1.0', 'end-1c'))
        if (64 < ord(ch) < 78) or (97 < ord(ch) < 110): 
            x = ord(ch)
            x = str(x) 
	    x += "\n"
            self.display.insert(END, x) 
        else: 
            y = ord(ch) 
            y = str(chr(y - 13))
	    y += "\n"
 	    self.display.insert(END, y) + "\n"
    def rot13(self):
	phrase = self.xinput.get('1.0', 'end-1c') 
        pos = 0 
        string = "" 
        while pos < len(phrase):  
            if phrase[pos] == " ":
                string = string + " "
            elif ord(phrase[pos]) < 64 or ord(phrase[pos]) > 110:
                string += phrase[pos]
            else:
                letter = phrase[pos] 
                string += rot13Chr(letter)
            pos += 1
	string += "\n"
        self.display.insert(END, string) 
    def quadraticformula(self):
	a = float(self.xinput.get('1.0', 'end-1c'))
	b = float(self.yinput.get('1.0', 'end-1c'))
	c = float(self.zinput.get('1.0', 'end-1c'))
	d = self.winput.get('1.0', 'end-1c')
        answer1 = (-1 * b + math.sqrt((b**2) - (4 * a * c))) / (2 * a)
        answer2 = (-1 * b - math.sqrt((b**2) - (4 * a * c))) / (2 * a)
        answer1 = str(answer1)
	answer2 = str(answer2)
	answer1 += "\n"
	answer2 += "\n"
	if w == "+":
	    self.display.insert(END, answer1)
	else:
            self.display.insert(END, answer2)

# Geometry
def volumeofsphere(radius):
        answer = (4/3)(math.pi)(radius ** 3)
        return answer

def volumeofcone(radius, height):
        answer = (radius ** 2)(math.pi)(height /3)
        return answer

def surfareaofsphere(radius):
        answer = 4 * (math.pi) * (radius ** 2)
        return answer

def surfareaofcone(radius, height):
        answer = (math.pi)(radius)(radius + (math.sqrt((height ** 2) + (radius ** 2))))
        return answer

def volumeofcylinder(radius, height):
        answer = (volumeofcone(radius, height)) * 3
        return answer

def surfareaofcylnder(radius, height):
        answer = (2 * math.pi * radius)(height + radius)
        return answer

def volumeofsquarepyramid(area, height):
        answer = (area * height) / 3

def surfareaofsquarepyramid(length, width, height):
        part1 = length * width
        part2 = length * math.sqrt(((length/2)**2) + (height**2))
        part3 = width * math.sqrt(((length/2)**2) + (height**2))
        answer = part1 + part2 + part3

def pythagoreantheorem(a, b):
        answer = math.sqrt((a**2) + (b**2))
        return answer

def distance(x1,y1,x2,y2):
        answer = pythagoreantheorem((x2 - x1), (y2 - y1))
        return answer  
    ########################
    #Creates the widgets for the window GUI buttons
    def createWidgets(self):
         ####DISPLAY BOX####
         displabel = Label(self, text="Display Output") 
         displabel.grid()

         self.display = Text(self, width="50", height="20", fg= "royal blue")
         self.display.grid(row=0, column=0)
         
         self.QUIT = Button(self, width="50", text="QUIT",bg="red", command=self.quit)
         self.QUIT.grid(row=1,column=0)
                        
         self.cls = Button(self, width="50", text="Clear the display box", command=self.CLS)
         self.cls.grid(row=2, column=0)

         ####MORE FUNCTIONS
         self.add = Button(self, width="10", text="x+y", bg="green", command=self.addition)
         self.add.grid(row=1, column=1)
         self.minus = Button(self, width="10", text="x-y", bg="green", command=self.subtraction)
         self.minus.grid(row=2, column=1)
         self.multi = Button(self, width="10", text="x*y", bg="green", command=self.multiplication)
         self.multi.grid(row=3, column=1)
         self.div = Button(self, width="10", text="x/y", bg="green", command=self.division)
         self.div.grid(row=4, column=1)
        

         ########################################
         self.carryx = Button(self, width="10", text="CARRY TO X (ANS)", bg="blue", command=self.carryX) #Makes a button with the parameter
         self.carryx.grid(row=5, column=1) #Places the button anywhere on the screen

         self.carryy = Button(self, width="10", text="CARRY TO Y (ANS)", bg="blue", command=self.carryY) #Makes a button with the parameter
         self.carryy.grid(row=6, column=1) #Places the button anywhere on the screen
         #XINPUT
         self.xinput = Text(self, width="10", height="1")
         xlabel = Label(self, text="                                                         X input:")
         xlabel.grid(row=7, column=0)
         self.xinput.grid(row=7, column=1)
             
         #YINPUT
         self.yinput = Text(self, width="10", height="1")
         ylabel = Label(self, text="                                                         Y input:")
         ylabel.grid(row=8, column=0)
         self.yinput.grid(row=8, column=1)
         
         #ZINPUT
         self.zinput = Text(self, height="1", width="10")
         zlabel = Label(self, text="                                                         Z input")
         zlabel.grid(row=9, column=0)
         self.zinput.grid(row=9, column=1)
	 
         #WINPUT
         self.winput = Text(self, height="1", width="10")
         wlabel = Label(self, text="                                                         X input")
         wlabel.grid(row=10, column=0)
         self.winput.grid(row=10, column=1)
	 
         #Math Module Functions go here
 
         self.ceil = Button(self, width="10", text="ceil(x)", command=self.ceiling)
         self.ceil.grid(row=1, column=2)

         self.fact = Button(self, width="10", text="factorial(x)", command=self.factorial)
         self.fact.grid(row=2, column=2)
 
         self.copys = Button(self, width="10", text="copysign(x)", command=self.copysign)
         self.copys.grid(row=3, column=2)

	 self.fabs = Button(self, width="10", text="abs(x)", command=self.absolute)
         self.fabs.grid(row=4, column=2)

	 self.fmod = Button(self, width="10", text="x mod y", command=self.modulus)
         self.fmod.grid(row=5, column=2)

	 self.flr = Button(self, width="10", text="floor(x)", command=self.floor)
         self.flr.grid(row=6, column=2)

         self.gcd = Button(self, width="10", text="gcd(x, y)", command=self.greatestcd)
         self.gcd.grid(row=7, column=2)
 
         self.exp = Button(self, width="10", text="exp(x)", command=self.exp_e)
         self.exp.grid(row=8, column=2)

 	 self.log = Button(self, width="10", text="log(x, y)", command=self.logarithm)
         self.log.grid(row=9, column=2)

	 self.log10 = Button(self, width="10", text="log10(x)", command=self.logten)
         self.log10.grid(row=10, column=2)

	 self.pow = Button(self, width="10", text="pow(x, y)", command=self.power)
         self.pow.grid(row=11, column=2)

	 self.deg = Button(self, width="10", text="deg(x)", command=self.degrees)
         self.deg.grid(row=12, column=2)

         self.rad = Button(self, width="10", text="rad(x)", command=self.radians)
         self.rad.grid(row=13, column=2)
	 
	#TRIG FUNCTIONS

         self.trig = Label(self, width="20", text="Trig Functions")
	 self.trig.grid(row=0, column=3)

	 self.sin = Button(self, width="20", text="sin(x)", command=self.sine)
         self.sin.grid(row=1, column=3)

         self.cos = Button(self, width="20", text="cos(x)", command=self.cosine)
         self.cos.grid(row=2, column=3)

	 self.tan = Button(self, width="20", text="tan(x)", command=self.tangent)
         self.tan.grid(row=3, column=3)
 
 	 self.asin = Button(self, width="20", text="asin(-pi/2<x<pi/2)", command=self.arcsin)
         self.asin.grid(row=4, column=3)

	 self.acos = Button(self, width="20", text="acos(-pi/2<x<pi/2)", command=self.arccos)
         self.acos.grid(row=5, column=3)

	 self.atan = Button(self, width="20", text="atan(-pi/2<x<pi/2)", command=self.arctan)
         self.atan.grid(row=6, column=3)

	 self.csc = Button(self, width="20", text="csc(x)", command=self.cosecant)
         self.csc.grid(row=7, column=3)

         self.sec = Button(self, width="20", text="sec(x)", command=self.secant)
         self.sec.grid(row=8, column=3)

	 self.cot = Button(self, width="20", text="cot(x)", command=self.cotangent)
         self.cot.grid(row=9, column=3)
 	
	 self.acsc = Button(self, width="20", text="acsc(x<-pi/2 , x>pi/2)", command=self.arccsc)
         self.acsc.grid(row=10, column=3)

	 self.asec = Button(self, width="20", text="asec(x<-pi/2, x>pi/2)", command=self.arcsec)
         self.asec.grid(row=11, column=3)

	 self.acot = Button(self, width="20", text="acot(x<-pi/2, x>pi/2)", command=self.arccot)
         self.acot.grid(row=12, column=3)
	#HYPERBOLIC FUNCTIONS

	 self.trig = Label(self, width="20", text="Hyperbolic Functions")
	 self.trig.grid(row=0, column=4)

   	 self.sinh = Button(self, width="20", text="sinh(x)", command=self.sineh)
         self.sinh.grid(row=1, column=4)
	
	 self.cosh = Button(self, width="20", text="cosh(x)", command=self.cosineh)
         self.cosh.grid(row=2, column=4)

	 self.tanh = Button(self, width="20", text="tanh(x)", command=self.tangenth)
         self.tanh.grid(row=3, column=4)

	 self.asinh = Button(self, width="20", text="asinh(x)", command=self.arcsineh)
         self.asinh.grid(row=4, column=4)

	 self.acosh = Button(self, width="20", text="acosh(x)", command=self.arccosineh)
         self.acosh.grid(row=5, column=4)

	 self.atanh = Button(self, width="20", text="atanh(x)", command=self.arctangenth)
         self.atanh.grid(row=6, column=4)

	 #CUSTOM FUNCTIONS
	 self.customf = Label(self, width="15", text="Custom Functions")
	 self.customf.grid(row=4, column=0)
	 self.permute = Button(self, width="15", text="xPy", command=self.permutations)
	 self.permute.grid(row=5, column=0)

	 self.combine = Button(self, width="15", text="xCy", command=self.combinations)
	 self.combine.grid(row=6, column=0)

	 self.geom = Button(self, width="15", text="geometric(x, y)", command=self.geometric)
	 self.geom.grid(row=7, column=0)

	 self.bincdf = Button(self, width="15", text="binomial_cdf(x, y, z, w)", command=self.binomialcdf)
	 self.bincdf.grid(row=8, column=0)

	 self.encrypt = Button(self, width="40", text="ROT13(x)", command=self.rot13Chr)
	 self.encrypt.grid(row=12, column=0)

	 self.decrypt = Button(self, width="40", text="decrypt ROT13(x)", command=self.rot13)
	 self.decrypt.grid(row=13, column=0)

	 
    #PUT ALL THE BUTTON CODE HERE
    ########################
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    #barebones stuff we need
root = Tk()
root.title("Calcu++")
app = Application(master=root)
app.mainloop()
root.destroy()
quit()
