from tkinter import *

root=Tk()

label=Label(root, text="INPUT:")

label.grid(row=0, column=0)

input_entry=Entry(root, width=42)

input_entry.grid(row=0, column=1, columnspan=4)



def click(num):

    current=input_entry.get()

    input_entry.delete(0, END)

    input_entry.insert(END, str(current) + str(num))



def add():

    global fnum

    global operation

    operation="+"

    fnum=float(input_entry.get())

    input_entry.delete(0, END)



def sub():

    global fnum

    global operation

    operation="-"

    fnum=float(input_entry.get())

    input_entry.delete(0, END)

def mul():

    global fnum

    global operation

    operation="*"

    fnum=float(input_entry.get())

    input_entry.delete(0, END)

def div():

    global fnum

    global operation

    operation="/"

    fnum=float(input_entry.get())

    input_entry.delete(0, END)



def clear():

    input_entry.delete(0, END)

def equal():

    try:

        global operation

        snum=float(input_entry.get())

        if operation == "+":

            result=fnum+snum

        elif operation == "-":

            result=fnum-snum

        elif operation =="*":

            result=fnum*snum

        elif operation == "/":

            if snum != 0:

                result=fnum/snum

            else:

                Messagebox.showerror("zero division error!!!")

        else:

            result="error"

        input_entry.delete(0, END)

        input_entry.insert(END, result)



    except ValueError:

        Messagebox.showerror("enter valid operation")



button1=Button(root, text="1", padx=35, pady=15, command=lambda: click(1))

button1.grid(row=1, column=0)

button2=Button(root, text="2", padx=35, pady=15, command=lambda: click(2))

button2.grid(row=1, column=1)

button3=Button(root, text="3", padx=35, pady=15, command=lambda: click(3))

button3.grid(row=1, column=2)

button4=Button(root, text="4", padx=35, pady=15, command=lambda: click(4))

button4.grid(row=2, column=0)

button5=Button(root, text="5", padx=35, pady=15, command=lambda: click(5))

button5.grid(row=2, column=1)

button6=Button(root, text="6", padx=35, pady=15, command=lambda: click(6))

button6.grid(row=2, column=2)

button7=Button(root, text="7", padx=35, pady=15, command=lambda: click(7))

button7.grid(row=3, column=0)

button8=Button(root, text="8", padx=35, pady=15, command=lambda: click(8))

button8.grid(row=3, column=1)

button9=Button(root, text="9", padx=35, pady=15, command=lambda: click(9))

button9.grid(row=3, column=2)

button0=Button(root, text="0", padx=35, pady=15, command=lambda: click(0))

button0.grid(row=4, column=1)



buttonadd=Button(root, text="+", padx=35, pady=15, command=add)

buttonadd.grid(row=4, column=0)

buttonsub=Button(root, text="-", padx=35, pady=15, command=sub)

buttonsub.grid(row=4, column=2)

buttonmul=Button(root, text="*", padx=35, pady=15, command=mul)

buttonmul.grid(row=3, column=3)

buttondiv=Button(root, text="/", padx=35, pady=15, command=div)

buttondiv.grid(row=2, column=3)

buttoneq=Button(root, text="=", padx=35, pady=15, command=equal, bg="light green")

buttoneq.grid(row=4, column=3)



buttonc=Button(root, text="AC", padx=31, pady=16, command=clear, background="orange red")

buttonc.grid(row=1, column=3)



root.mainloop()