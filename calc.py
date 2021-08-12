from tkinter import*
root=Tk()
root.title("Calculator")
root.iconbitmap("/Users/inishbashyal/Attendance Management System/calculator2.ico")

exp = ""   #we have expression value shown in the entry
eqn=StringVar()
root.minsize(height=530, width=460)
root.maxsize(height=530, width=460)

e=Entry(root, width=45, borderwidth=5, text=eqn)
e.grid(row=0, column=0, columnspan=50, padx=10, pady=10)

def button_click(number):     #function to update expression
    global exp
    exp=exp+str(number)     #concatenation of string
    eqn.set(exp)        #change the expression in the entry when we click

def button_clear():
    global exp
    exp=''      #as we use string var so for clearing the content of entry
    eqn.set('')


def button_equal(): #function to evaluate the final expression
    global exp
    final=str(eval(exp))   #eval runs the python code or expression which is passed as an argument
    eqn.set(final)
    exp=''     #initializing the expression by empty string

zero=PhotoImage(file='0.png')
one=PhotoImage(file='1.png')
two=PhotoImage(file='2.png')
three=PhotoImage(file='3.png')
four=PhotoImage(file='4.png')
five=PhotoImage(file='5.png')
six=PhotoImage(file='6.png')
seven=PhotoImage(file='7.png')
eight=PhotoImage(file='8.png')
nine=PhotoImage(file='9.png')
add=PhotoImage(file='add.png')
sub=PhotoImage(file='subtract.png')
multi=PhotoImage(file='multiply.png')
div=PhotoImage(file='divide.png')
dec=PhotoImage(file='decimal.png')
clear=PhotoImage(file='clear.png')
equal=PhotoImage(file='equal.png')


button_0=Button(root, image=zero, command=lambda: button_click(0) )
button_1=Button(root, image=one, command=lambda: button_click(1))
button_2=Button(root, image=two, command=lambda: button_click(2) )
button_3=Button(root, image=three, command=lambda: button_click(3) )
button_4=Button(root, image=four, command=lambda: button_click(4) )
button_5=Button(root, image=five, command=lambda: button_click(5) )
button_6=Button(root, image=six, command=lambda: button_click(6) )
button_7=Button(root, image=seven, command=lambda: button_click(7) )
button_8=Button(root, image=eight, command=lambda: button_click(8) )
button_9=Button(root, image=nine, command=lambda: button_click(9) )
button_add=Button(root, image=add, command=lambda: button_click('+'))
button_subtract=Button(root, image=sub, command=lambda: button_click('-'))
button_divide=Button(root, image=div, command=lambda: button_click('/'))
button_multiply=Button(root, image=multi, command=lambda: button_click('*'))
button_decimal=Button(root, image=dec, command=lambda: button_click('.'))


button_equal=Button(root, image=equal, command=button_equal)
button_clear=Button(root, image=clear, command=button_clear)



button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_subtract.grid(row=3,column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)


button_clear.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_0.place(x=-10,y=437)
button_decimal.grid(row=5, column=2)
button_equal.grid(row=5, column=3)


#starting the gui
root.mainloop()
