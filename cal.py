from tkinter import *
import math

total=0 
expression = ""

def press(num):    
    global expression 
    expression = expression + str(num) 
    equation.set(expression) 

def pressingEqual():
    global expression
    global total
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Syntax Error")
    expression = ""


def squareroot():
    try:
        global total
        global expression
        if isinstance (expression,int):
            expression = int(expression)
            total = math.sqrt(int(expression))
            equation.set(total)

    except:
        expression = "Syntax Error"
        
def sine():
    try:
        global total
        global expression
        if isinstance (expression,int):
            expression = int(expression)
            total = math.sinh(int(expression))
            equation.set(total)
        else:
            expression = float(expression)
            total = math.sinh(float(expression))
            equation.set(total)
            
    except:
        expression = "Syntax Error"
def cosine():
    try:
        global total
        global expression
        if isinstance(expression,int):
            expression = int(expression)
            total = math.cos(int(expression))
            equation.set(total)
        else:
            expression = float(expression)
            total = math.cos(float(expression))
            equation.set(total)
    except:
        expression = "Syntax Error"
def tangent():
    try:
        global total
        global expression
        if isinstance(expression,int):
            expression = int(expression)
            total = math.tan(int(expression))
            equation.set(total)
        else:
            expression = float(expression)
            total = math.tan(float(expression))
            equation.set(total)
    except:
        expression = "Syntax Error"
def pi():
    try:
        global total
        global expression
        if isinstance(expression,int):
            expression = int(expression)
            total = int(expression)* 3.141592
            equation.set(total)
        else:
            expression = float(expression)
            total = float(expression)*3.141592
            equation.set(total)
    except:
        expression = "Syntax Error"
            
def factorial():
    try:
        global total
        global expression
        if isinstance(expression,int):
            expression = int(expression)
            total = math.factorial(int(expression))
            equation.set(total)
        else:
            expression = float(expression)
            total = math.factorial(int(expression))
            equation.set(total)
    except:
        expression = "Syntax Error"
def x2():
    try:
        global total
        global expression
        if isinstance(expression,int):
            expression = int(expression)
            total = int(expression)** 2
            equation.set(total)
        else:
            expression = float(expression)
            total = float(expression)** 2
            equation.set(total)
    except:
        expression = "Syntax Error"
def expo():
    global expression
    global total
    total=float(expression)**2
    equation.set(total)

retrieve= 0 
memory= 0
def memplus():
    global expression
    global memory
    global retrieve
    numbers="0123456789.-"
    char=""
    for i in str(expression):
        if i in numbers:
            print(i)
            continue
        else:
            char+=i
    if char =="":
        equation.set("Successfully Stored!!")
        print(expression)
        expression=(expression)
        memory+=(expression)
        retrieve=memory
    else:
        equation.set("ERROR")

    expression=""
def M():
    global memory
    equation.set(memory)
def Mc():
    global memory
    equation.set("Cleared")
    memory=0
def Mr():
    global retrieve
    equation.set(retrieve)
def factor():
    global expression
    expression+="!"
    equation.set(expression)

def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
  
  
# Driver code 
if __name__ == "__main__": 

    gui = Tk() 

    gui.configure() 
    
    gui.title("Pseudo-Scientific Calculator") 
    

  
    equation = StringVar() 
   
    expression_field = Entry(gui,font=('kaushan script',22,'bold'),width=15, textvariable=equation,bd=15,insertwidth=5,bg="pink",justify="right") 

    expression_field.grid(row=0,column=0, columnspan=7,pady=20)
 
  
   
    button1 = Button(gui, text=' 1 ', fg='black', bg='pink', 
                     command=lambda: press(1), height=4, width=7) 
    button1.grid(row=2, column=0) 
  
    button2 = Button(gui, text=' 2 ', fg='black', bg='pink', 
                     command=lambda: press(2), height=4, width=7) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(gui, text=' 3 ', fg='black', bg='pink', 
                     command=lambda: press(3), height=4, width=7) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(gui, text=' 4 ', fg='black', bg='pink',
                     command=lambda: press(4), height=4, width=7) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(gui, text=' 5 ', fg='black', bg='pink', 
                     command=lambda: press(5), height=4, width=7) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(gui, text=' 6 ', fg='black', bg='pink', 
                     command=lambda: press(6), height=4, width=7) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(gui, text=' 7 ', fg='black', bg='pink', 
                     command=lambda: press(7), height=4, width=7) 
    button7.grid(row=4, column=0) 
  
    button8 = Button(gui, text=' 8 ', fg='black', bg='pink', 
                     command=lambda: press(8), height=4, width=7) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(gui, text=' 9 ', fg='black', bg='pink', 
                     command=lambda: press(9), height=4, width=7) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(gui, text=' 0 ', fg='black', bg='pink', 
                     command=lambda: press(0), height=4, width=7) 
    button0.grid(row=5, column=1)
    button_dot = Button(gui, text=' . ', fg='black', bg='pink', 
                     command=lambda: press("."), height=4, width=7) 
    button_dot.grid(row=5, column=0) 
  
    plus = Button(gui, text=' + ', fg='black', bg='sky blue', 
                  command=lambda: press("+"), height=4, width=7) 
    plus.grid(row=2, column=3) 
  
    minus = Button(gui, text=' - ', fg='black', bg='sky blue', 
                   command=lambda: press("-"), height=4, width=7) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(gui, text=' * ', fg='black', bg='sky blue', 
                      command=lambda: press("*"), height=4, width=7) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(gui, text=' / ', fg='black', bg='sky blue', 
                    command=lambda: press("/"), height=4, width=7) 
    divide.grid(row=5, column=2) 
  
    equal = Button(gui, text=' = ', fg='black', bg='gray', 
                   command=pressingEqual, height=4, width=7) 
    equal.grid(row=5, column=5) 
    squareroot= Button(gui, text=' √ ', fg='black', bg='#D4D4F7', 
                   command=squareroot, height=4, width=7) 
    squareroot.grid(row=2, column=5)
    cos= Button(gui, text='cos', fg='black', bg='#D4D4F7', 
                   command=cosine, height=4, width=7) 
    cos.grid(row=3, column=5)
    tan= Button(gui, text='tan', fg='black', bg='#D4D4F7', 
                   command=tangent, height=4, width=7) 
    tan.grid(row=4, column=5)
    sin= Button(gui, text='sin', fg='black', bg='#D4D4F7', 
                   command=sine, height=4, width=7) 
    sin.grid(row=5, column=3) 
    clear = Button(gui, text='Clear', fg='black', bg='gray', 
                   command=clear, height=4, width=15) 
    clear.grid(row=1, column='4',columnspan=14)
    Button(gui, text='M+', fg='black', bg='pink', 
                   command=memplus, height=4, width=7).grid(row=1, column='0')
    Button(gui, text='Mr', fg='black', bg='pink', 
                   command=Mr, height=4, width=7).grid(row=1, column='1')
    Button(gui, text='Mc', fg='black', bg='pink', 
                   command=Mc, height=4, width=7).grid(row=1, column='2')
    Button(gui, text='M', fg='black', bg='pink', 
                   command=M, height=4, width=7).grid(row=1, column='3')
    Button(gui, text='exp', fg='black', bg='#D4D4F7', 
                   command=expo, height=4,width=7).grid(row=2, column='4')
    Button(gui, text='π', fg='black', bg='#D4D4F7', 
                   command=pi, height=4, width=7).grid(row=3, column='4')
    Button(gui, text='n!', fg='black', bg='#D4D4F7', 
                   command=factorial, height=4, width=7).grid(row=4, column='4')
    Button(gui, text='x²', fg='black', bg='#D4D4F7', 
                   command=x2, height=4, width=7).grid(row=5, column='4')
    
  
    # start the GUI 
    gui.mainloop() 
