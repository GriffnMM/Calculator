#-*-coding: utf-8-*-
from Tkinter import *
import math

def clearstuff():
    e.delete(0,END)

class calc:
 def getandreplace(self):
  """replace x with * and ÷ with /"""
  
  self.expression = self.e.get()
  self.newtext=self.expression.replace(self.newdiv,'/')
  self.newtext=self.newtext.replace('x','*')

 def equals(self):
  """when the equal button is pressed"""

  self.getandreplace()
  try: 
   self.value= eval(self.newtext)
  except SyntaxError or NameError:
   self.e.delete(0,END)
   self.e.insert(0,'Invalid Input')
  else:
   self.e.delete(0,END)
   self.e.insert(0,self.value)
 
 def squareroot(self):
  """squareroot method"""
  
  self.getandreplace()
  try: 
   self.value= eval(self.newtext) 
  except SyntaxError or NameError:
   self.e.delete(0,END)
   self.e.insert(0,'Invalid Input')
  else:
   self.sqrtval=math.sqrt(self.value)
   self.e.delete(0,END)
   self.e.insert(0,self.sqrtval)

 def square(self):
  """square method"""
  
  self.getandreplace()
  try: 
   self.value= eval(self.newtext) 
  except SyntaxError or NameError:
   self.e.delete(0,END)
   self.e.insert(0,'Invalid Input')
  else:
   self.sqval=math.pow(self.value,2)
   self.e.delete(0,END)
   self.e.insert(0,self.sqval)
 
 def clearall(self): 
  """when clear button is pressed,clears the text input area"""
  self.e.delete(0,END)
 
 def clear1(self):
  self.txt=self.e.get()[:-1]
  self.e.delete(0,END)
  self.e.insert(0,self.txt)

 def action(self,argi): 
  """pressed button's value is inserted into the end of the text area"""
  self.e.insert(END,argi)
 
 def __init__(self,master):
  """Constructor method"""
  master.title('Calulator') 
  master.geometry()
  self.e = Entry(master,width=50)
  self.e.grid(row=0,column=0,columnspan=6,pady=3)
  self.e.focus_set()
    
  self.div='÷'
  self.newdiv=self.div.decode('utf-8')

  Button(master,text="=",width=6,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
  
  Button(master,text='AC',width=6,command=lambda:self.clearall()).grid(row=1, column=4)
  
  Button(master,text='C',width=6,command=lambda:self.clear1()).grid(row=1, column=5)
  
  Button(master,text="+",width=6,command=lambda:self.action('+')).grid(row=4, column=3)
  
  Button(master,text="x",width=6,command=lambda:self.action('x')).grid(row=2, column=3)
  
  Button(master,text="-",width=6,command=lambda:self.action('-')).grid(row=3, column=3)
  
  Button(master,text="÷",width=6,command=lambda:self.action(self.newdiv)).grid(row=1, column=3) 
  
  Button(master,text="%",width=6,command=lambda:self.action('%')).grid(row=4, column=2)
  
  Button(master,text="7",width=6,command=lambda:self.action('7')).grid(row=1, column=0)
  
  Button(master,text="8",width=6,command=lambda:self.action(8)).grid(row=1, column=1)
  
  Button(master,text="9",width=6,command=lambda:self.action(9)).grid(row=1, column=2)
  
  Button(master,text="4",width=6,command=lambda:self.action(4)).grid(row=2, column=0)
  
  Button(master,text="5",width=6,command=lambda:self.action(5)).grid(row=2, column=1)
  
  Button(master,text="6",width=6,command=lambda:self.action(6)).grid(row=2, column=2)
  
  Button(master,text="1",width=6,command=lambda:self.action(1)).grid(row=3, column=0)
  
  Button(master,text="2",width=6,command=lambda:self.action(2)).grid(row=3, column=1)
  
  Button(master,text="3",width=6,command=lambda:self.action(3)).grid(row=3, column=2)
  
  Button(master,text="0",width=6,command=lambda:self.action(0)).grid(row=4, column=0)
  
  Button(master,text=".",width=6,command=lambda:self.action('.')).grid(row=4, column=1)
  
  Button(master,text="(",width=6,command=lambda:self.action('(')).grid(row=2, column=4)
  
  Button(master,text=")",width=6,command=lambda:self.action(')')).grid(row=2, column=5)
  
  Button(master,text="√",width=6,command=lambda:self.squareroot()).grid(row=3, column=4)
  
  Button(master,text="x²",width=6,command=lambda:self.square()).grid(row=3, column=5)
    
def openfileW():
  print "it works"
    
def openfileR():
  fj=open("Readme.txt", 'w')
  inputs = master.get(0, END)
  for i in inputs:
   fj.write(i+"\n")
  fj.close()

root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save", command=openfileR)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Clear", command=openfileW)

menubar.add_cascade(label="Edit", menu=editmenu)


root.config(menu=menubar)



obj=calc(root)
root.mainloop()