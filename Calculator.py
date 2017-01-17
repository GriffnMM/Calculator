from Tkinter import *
import math






root = Tk()
root.title("calculator")

title = Label(root, text="The greatest calculator ever made!                      ", bg = "magenta")
title.grid(row=0, column=0, sticky=EW, columnspan=6)

menubar=Menu(root)
filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="Clear")
filemenu.add_separator()
filemenu.add_command(label="Save")

menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)

entry1 = Entry(root)
entry1.grid(row=1, column=0, sticky=EW, columnspan=6)

button1 = Button(root, text="1")
button1.grid(row=4, column=0, sticky=EW)

button2 = Button(root, text="2")
button2.grid(row=4, column=1, sticky=EW)

button3 = Button(root, text="3")
button3.grid(row=4, column=2, sticky=EW)

button4 = Button(root, text="4")
button4.grid(row=3, column=0, sticky=EW)

button5 = Button(root, text="5")
button5.grid(row=3, column=1, sticky=EW)

button6 = Button(root, text="6")
button6.grid(row=3, column=2, sticky=EW)

button7 = Button(root, text="7")
button7.grid(row=2, column=0, sticky=EW)

button8 = Button(root, text="8")
button8.grid(row=2, column=1, sticky=EW)

button9 = Button(root, text="9")
button9.grid(row=2, column=2, sticky=EW)

button0 = Button(root, text="0")
button0.grid(row=5, column=0, sticky=EW)

buttone = Button(root, text="=")
buttone.grid(row=5, column=1, sticky=EW, columnspan=2)

buttonplus = Button(root, text="+")
buttonplus.grid(row=2, column=3, sticky=EW)

buttonminus = Button(root, text="-")
buttonminus.grid(row=3, column=3, sticky=EW)

buttonmult = Button(root, text="x")
buttonmult.grid(row=4, column=3, sticky=EW)

buttondiv = Button(root, text="/")
buttondiv.grid(row=5, column=3, sticky=EW)

mainloop()