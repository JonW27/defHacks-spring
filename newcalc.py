import Tkinter, math #main bits of code go here
from Tkinter import *

class Application(Frame):
    #Keep the functions here, let's use .pack() instead of .pack()
    #DEFINE THE FUNCTIONS HERE
    def functionLoad(self):
        #newfile = open(filename, 'rw')
        #read = newfile.read()
        filename = self.xinput.get('1.0', 'end-1c')
        print filename
        func = self.yinput.get('1.0', 'end-1c')#NEEDS PARAMETERS TO BE ENTERED
        e = open(filename, 'rU')
        f = e.read()
        g = f.split("def")[0]
        print repr(g)
        
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
    def floatsum(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.fsum(x))
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
    def logtwo(self):
        x = self.xinput.get('1.0', 'end-1c')
        x = float(x)
        z = float(math.log2(x))
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
        rand = str(rand)
        rand = rand + "\n"
        self.display.insert(END, rand)
    def opens(self):
        file = tkfile.askopenfile(parent=root, mode='rb', title="select a file")
        if file != None:
            contents = file.read()
            self.display.insert('1.0', contents)
            file.close()
    def save(self):
        file = tkfile.asksaveasfile(mode='w')
        if file != None:
            data = self.display.get('1.0', END + '-1c')
            file.write(data)
            file.close()
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
        import math

# AP Statistics
def permutations(n,r):
    answer = (math.factorial(n))/((math.factorial(r))(math.factorial(n - r)))
    return answer
    
def combinations(n,r):
    answer = (math.factorial(n)/(math.factorial(n - 3))
    return answer

def geometric(p,x):
    answer = p * ((1 - p) ** (x - 1))
    return answer

def hypergeometric(total, smplsize, sucinpop, sucinsam):
    answer = ((combinations(sucinpop, sucinsam))(combinations((total - sucinpop), (smplsize - sucinsam)))) / (combinations(total, smplsize))
    return answer

def binomialcdf(n,x,p):
    answer = ((math.factorial(n)) / ((math.factorial(n - x))(math.factorial(x)))) * (p ** x)((1 - p) ** (n - x))
    return answer

# Encryption
def rot13Chr(ch): 
    if (64 < ord(ch) < 78) or (97 < ord(ch) < 110): 
        x = ord(ch) 
        return chr(x + 13) 
    else: 
        y = ord(ch) 
        return chr(y - 13) 
 
def rot13(phrase): 
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
    return string

# Trig/ Algebra 2
def quadraticformula(a,b,c):
    answer1 = (-b + math.sqrt((b**2) - (4 * a * c))) / (2 * a)
    answer2 = (-b - math.sqrt((b**2) - (4 * a * c))) / (2 * a)
    return answer1
    return answer2

def csc(angle):
    answer = (1 / math.sin(angle))(math.pi / 180)
    return answer

def sec(angle):
    answer = (1 / math.cos(angle))(math.pi / 180)
    return answer

def cot(angle):
    answer = (1 / math.tan(angle))(math.pi / 180)
    return answer

def cis(angle):
    answer =  math.sin(angle) + "i" + math.cos(angle) + "i"
    return answer

              
                      
    ########################
    #Creates the widgets for the window GUI buttons
    def createWidgets(self):
         ####DISPLAY BOX####
         displabel = Label(self)
         displabel["text"] = "Display Output" 
         displabel.pack()

         self.display = Text(self)
         self.display["height"] = "10"
         self.display["width"] = "50"
         self.display["fg"] = "royal blue"

         self.display.pack()
         
         self.QUIT = Button(self)
         self.QUIT["text"] = "QUIT"
         self.QUIT["bg"]   = "red"
         self.QUIT["command"] =  self.quit

         self.QUIT.pack(fill=X)
                        
         self.loadButton = Button(self)
         self.loadButton["text"] = "Load a custom function"
         self.loadButton["command"] = self.functionLoad
         self.loadButton.pack()
         
         ####MORE FUNCTIONS
         self.add = Button(self)
         self.add["text"] = "x + y"
         self.add["bg"] = "green"
         self.add["command"] = self.addition
         self.add.pack(fill=X)
         self.minus = Button(self)
         self.minus["text"] = "x - y"
         self.minus["bg"] = "green"
         self.minus["command"] = self.subtraction
         self.minus.pack(fill=X)
         self.multi = Button(self)
         self.multi["text"] = "x * y"
         self.multi["bg"] = "green"
         self.multi["command"] = self.multiplication
         self.multi.pack(fill=X)
         self.div = Button(self)
         self.div["text"] = "x / y"
         self.div["bg"] = "green"
         self.div["command"] = self.division
         self.div.pack(fill=X)
        
         self.opensfile = Button(self)

         self.opensfile["text"] = "Open a custom function file"
         self.opensfile["bg"] = "yellow"
         self.opensfile["command"] = self.opens
         
         self.opensfile.pack(fill=X)        

         self.savefile = Button(self)
         self.savefile["text"] = "Save custom file"
         self.savefile["bg"] = "yellow"
         self.savefile["command"] = self.save
 
 
         self.savefile.pack(fill=X)

         ########################################
         self.carryx = Button(self) #Makes a button with the parameter
         self.carryx["text"] = "CARRY TO X (ANS)" #text on button
         self.carryx["bg"]   = "blue"
         self.carryx["fg"] = "white"
         self.carryx["command"] =  self.carryX #Command of the button,
                                         #This command closes the program.
         self.carryx.pack(fill=X) #Places the button anywhere on the screen



         self.carryy = Button(self) #Makes a button with the parameter
         self.carryy["text"] = "CARRY TO Y (ANS)" #text on button
         self.carryy["bg"]   = "blue"
         self.carryy["fg"] = "white"
         self.carryy["command"] =  self.carryY #Command of the button,
                                         #This command closes the program.
         self.carryy.pack(fill=X) #Places the button anywhere on the screen
         #XINPUT
         self.xinput = Text(self)
         self.xinput["height"] = "2"
         self.xinput["width"] = "15"

         xlabel = Label(self)
         xlabel["text"] = "X input"

         xlabel.pack()

         self.xinput.pack({"side":"top"})
             
         #YINPUT
         self.yinput = Text(self)
         self.yinput["height"] = "2"
         self.yinput["width"] = "15"

         ylabel = Label(self)
         ylabel["text"] = "Y input"

         ylabel.pack()

         self.yinput.pack({"side":"top"})
         
         #Math Module Functions go here
 
         self.ceil = Button(self)
         self.ceil["text"] = "ceil(x)"
         self.ceil["command"] = self.ceiling

         self.ceil.pack({"side":"left"})

         self.fact = Button(self)
         self.fact["text"] = "factorial(x)"
         self.fact["command"] = self.factorial
 
         self.fact.pack({"side":"left"})
 
         self.copys = Button(self)
         self.copys["text"] = "copysign(x)"
         self.copys["command"] = self.copysign

         self.copys.pack({"side":"left"})
 
         self.fabs = Button(self)
         self.fabs["text"] = "fabs(x)"
         self.fabs["command"] = self.absolute

         self.fabs.pack({"side":"left"})

         self.fmod = Button(self)
         self.fmod["text"] = "fmod(x)"
         self.fmod["command"] = self.modulus

         self.fmod.pack({"side":"left"})

         self.flr = Button(self)
         self.flr["text"] = "floor(x)"
         self.flr["command"] = self.floor

         self.flr.pack({"side":"left"})

         self.fsum = Button(self)
         self.fsum["text"] = "fsum(x)"
         self.fsum["command"] = self.floatsum

         self.fsum.pack({"side":"left"})

         self.gcd = Button(self)
         self.gcd["text"] = "gcd(x)"
         self.gcd["command"] = self.greatestcd
         
         self.gcd.pack({"side":"left"})
 
         self.exp = Button(self)
         self.exp["text"] = "exp(x)"
         self.exp["command"] = self.exp
 
         self.exp.pack({"side":"left"})

         self.log = Button(self)
         self.log["text"] = "log(x, y)"
         self.log["command"] = self.logarithm
 
         self.log.pack({"side":"left"})

         self.log10 = Button(self)
         self.log10["text"] = "log10(x)"
         self.log10["command"] = self.logten

         self.log10.pack({"side":"left"})

         self.pow = Button(self)
         self.pow["text"] = "pow(x, y)"
         self.pow["command"] = self.power

         self.pow.pack({"side":"left"})

         self.deg = Button(self)
         self.deg["text"] = "deg(x)"
         self.deg["command"] = self.degrees

         self.deg.pack({"side":"left"})

         self.rad = Button(self)
         self.rad["text"] = "rad(x)"
         self.rad["command"] = self.radians
        
         self.rad.pack({"side":"left"})

         self.sin = Button(self)
         self.sin["text"] = "sin(x)"
         self.sin["command"] = self.sine

         self.sin.pack({"side":"left"})

         self.cos = Button(self)
         self.cos["text"] = "cos(x)"
         self.cos["command"] = self.cosine

         self.cos.pack({"side":"left"})

         self.tan = Button(self)
         self.tan["text"] = "tan(x)"
         self.tan["command"] = self.tangent

         self.tan.pack({"side":"left"})
 
         self.asin = Button(self)
         self.asin["text"] = "asin(x)"
         self.asin["command"] = self.arcsin
 
         self.asin.pack({"side":"left"})

         self.acos = Button(self)
         self.acos["text"] = "acos(x)"
         self.acos["command"] = self.arccos

         self.acos.pack({"side":"left"})

         self.atan = Button(self)
         self.atan["text"] = "atan(x)"
         self.atan["command"] = self.arctan

         self.atan.pack({"side":"left"})
    #PUT ALL THE BUTTON CODE HERE
    ########################
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    #barebones stuff we need
root = Tk()
root.title("Calcu++")
app = Application(master=root)
app.mainloop()
root.destroy()
quit()
