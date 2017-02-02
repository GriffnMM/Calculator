# -*- coding: utf-8 -*-
from Tkinter import *
import math



def openfileW():
  entry1.delete(0,END)
    
def openfileR():
    fj=open("Readme.txt", 'w')
    inputs = entry1.get()
    fj.write(inputs)
    fj.close()
  
def openfileQ():
    fj=open("Readme.txt", 'w')
    fj.get()
    entry1.insert(END,fj)
    fj.close
    
def clear():
    entry1.delete(0, END)
    

def addtolist1():
    entrytxt="1"
    entry1.insert(END,entrytxt)
    
def addtolist2():
    entrytxt="2"
    entry1.insert(END,entrytxt)
    
def addtolist3():
    entrytxt="3"
    entry1.insert(END,entrytxt)
    
def addtolist4():
    entrytxt="4"
    entry1.insert(END,entrytxt)
    
def addtolist5():
    entrytxt="5"
    entry1.insert(END,entrytxt)
    
def addtolist6():
    entrytxt="6"
    entry1.insert(END,entrytxt)
    
def addtolist7():
    entrytxt="7"
    entry1.insert(END,entrytxt)
    
def addtolist8():
    entrytxt="8"
    entry1.insert(END,entrytxt)

def addtolist9():
    entrytxt="9"
    entry1.insert(END,entrytxt)
    
def addtolist0():
    entrytxt="0"
    entry1.insert(END,entrytxt)
    
def addtolistl():
    entrytxt="."
    entry1.insert(END,entrytxt)

def equals():
    equation = entry1.get()
    index = 0
    for i in equation:
        if i == "+":
            listofnumbers = equation.split('+',1)
            first = float(listofnumbers[0])
            second = float(listofnumbers[1])
            answer = first+second
            entry1.delete(0,END)
            entry1.insert(0,answer)
        elif i == "-":
            listofnumbers = equation.split('-',1)
            first = float(listofnumbers[0])
            second = float(listofnumbers[1])
            answer = first-second
            entry1.delete(0,END)
            entry1.insert(0,answer)
        elif i == "x":
            listofnumbers = equation.split('x',1)
            first = float(listofnumbers[0])
            second = float(listofnumbers[1])
            answer = first*second
            entry1.delete(0,END)
            entry1.insert(0,answer)
        elif i == "/":
            listofnumbers = equation.split('/',1)
            first = float(listofnumbers[0])
            second = float(listofnumbers[1])     
            answer = first/second
            entry1.delete(0,END)
            entry1.insert(0,answer)               
        index = index + 1
        
def sq():
    eq=entry1.get()
    ew=float(eq)
    answer=ew**2
    entry1.delete(0,END)
    entry1.insert(0,answer)
    
def percent():
    answer = entry1.get()
    first = float(answer)
    answer = first/100
    entry1.delete(0,END)
    entry1.insert(0,answer)  
    
def sqrt():
    eq=entry1.get()
    ew=float(eq)
    ans=ew**(.5)
    entry1.delete(0,END)
    entry1.insert(0,ans)
    
def action(argi): 
  entry1.insert(END,argi)
  
def addition():
    entrytxt="+"
    entry1.insert(END,entrytxt)
    
def multiply():
    entrytxt="x"
    entry1.insert(END,entrytxt)
    
def subtraction():
    entrytxt="-"
    entry1.insert(END,entrytxt)
    
def div():
    entrytxt="/"
    entry1.insert(END,entrytxt)    
root = Tk()

entry1 = Entry(root)
entry1.grid(row=0, column=1, columnspan=6, sticky=EW)


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=openfileR)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_separator()
filemenu.add_command(label="Open", command=openfileQ)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Clear", command=openfileW)


buttona=Button(root,text="=",width=6,command=equals)
buttona.grid(row=5, column=5,columnspan=2,sticky=EW)

  
buttonc=Button(root,text='C',width=6,command=clear)
buttonc.grid(row=2, column=5)
  
buttond=Button(root,text="+",width=6,command=addition)
buttond.grid(row=5, column=4)
  
buttone=Button(root,text="x",width=6,command=multiply)
buttone.grid(row=3, column=4)
  
buttonf=Button(root,text="-",width=6,command=subtraction)
buttonf.grid(row=4, column=4)
  
buttong=Button(root,text="÷",width=6,command=div)
buttong.grid(row=2, column=4) 
  
buttonh=Button(root,text="%",width=6,command=percent).grid(row=5, column=3)
  
button7=Button(root,text="7",width=6,command=addtolist7).grid(row=2, column=1)
  
button8=Button(root,text="8",width=6,command=addtolist8).grid(row=2, column=2)
  
button9=Button(root,text="9",width=6,command=addtolist9).grid(row=2, column=3)
  
button4=Button(root,text="4",width=6,command=addtolist4).grid(row=3, column=1)
  
button5=Button(root,text="5",width=6,command=addtolist5).grid(row=3, column=2)
  
button6=Button(root,text="6",width=6,command=addtolist6).grid(row=3, column=3)
  
button1=Button(root,text="1",width=6,command=addtolist1).grid(row=4, column=1)
  
button2=Button(root,text="2",width=6,command=addtolist2).grid(row=4, column=2)
  
button3=Button(root,text="3",width=6,command=addtolist3).grid(row=4, column=3)

button0=Button(root,text="0",width=6,command=addtolist0).grid(row=5, column=1)
  
buttoni=Button(root,text=".",width=6,command=addtolistl).grid(row=5, column=2)
    
buttonnl=Button(root,text="√",width=6,command=sqrt).grid(row=4, column=5)
  
buttonm=Button(root,text="x²",width=6,command=sq).grid(row=3, column=5)

menubar.add_cascade(label="Edit", menu=editmenu)


root.config(menu=menubar)




root.mainloop()