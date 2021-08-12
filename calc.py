from tkinter import*
root=Tk()

root.title("Calculator")
root.iconbitmap("/Users/inishbashyal/Attendance Management System/calculator2.ico")
root.configure(background="grey")
root.minsize(height=590, width=490)
root.maxsize(height=590, width=490)


exp = ""   #we have expression value shown in the entry
eqn=StringVar()

e=Entry(root, width=35, borderwidth=5, text=eqn, font=("Calibri",18))
e.place(height=70, width=472)
e.configure(background="black", fg="white")
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


button_0=Button(root, image=zero, command=lambda: button_click(0), height=83, width=200 )
button_1=Button(root, image=one, command=lambda: button_click(1), height=83, width=107)
button_2=Button(root, image=two, command=lambda: button_click(2), height=83, width=107 )
button_3=Button(root, image=three, command=lambda: button_click(3), height=83, width=107 )
button_4=Button(root, image=four, command=lambda: button_click(4), height=83, width=107 )
button_5=Button(root, image=five, command=lambda: button_click(5), height=83, width=107 )
button_6=Button(root, image=six, command=lambda: button_click(6) , height=83, width=107)
button_7=Button(root, image=seven, command=lambda: button_click(7), height=83, width=107 )
button_8=Button(root, image=eight, command=lambda: button_click(8), height=83, width=107 )
button_9=Button(root, image=nine, command=lambda: button_click(9), height=83, width=107 )
button_add=Button(root, image=add, command=lambda: button_click('+'), height=83, width=107)
button_subtract=Button(root, image=sub, command=lambda: button_click('-'), height=83, width=107)
button_divide=Button(root, image=div, command=lambda: button_click('/'), height=83, width=107)
button_multiply=Button(root, image=multi, command=lambda: button_click('*'), height=83, width=107)
button_decimal=Button(root, image=dec, command=lambda: button_click('.'), height=83, width=107)


button_equal=Button(root, image=equal, command=button_equal, height=83, width=107)
button_clear=Button(root, image=clear, command=button_clear, height=83, width=107)


button_0.place(x=2,y=455)
button_decimal.place(x=230,y=455)
button_equal.place(x=360,y=455)

button_1.place(x=0,y=360)
button_2.place(x=120,y=360)
button_3.place(x=240,y=360)
button_add.place(x=360,y=360)

button_4.place(x=0,y=265)
button_5.place(x=120,y=265)
button_6.place(x=240,y=265)
button_subtract.place(x=360,y=265)

button_7.place(x=0,y=170)
button_8.place(x=120,y=170)
button_9.place(x=240,y=170)
button_multiply.place(x=360,y=170)


button_clear.place(x=240,y=75)
button_divide.place(x=360,y=75)

#starting the gui
root.mainloop()
