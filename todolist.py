from tkinter import *

root=Tk()

root.title("TODOLIST")



box=Listbox(root, width=60, height=15, font=("helvicta", 10))

box.grid(row=1, column=0, columnspan=3, padx=40, pady=20)



entry=Entry(root, width=35, font=("helvicta", 10))

entry.grid(row=2, column=0)





def addtask():

    task = entry.get()

    if task:

        box.insert(END, task)

    entry.delete(0, END)





def deletetask():

    try:

        task = box.curselection()[0]

        box.delete(task)

    except IndexError:

        pass



 #markasdone function      

def markdone():

    try:

        task_index = box.curselection()[0]

        task = box.get(task_index)

        marked_task = task + " ✔"

        box.delete(task_index)  

        box.insert(task_index, marked_task)  

        box.itemconfig(task_index, {'bg': 'light green'})  



    except IndexError:

        pass





#buttons

button_add=Button(root, text="ADD_TASK", padx=5, pady=5, command= addtask)

button_add.grid(row=2, column=1, columnspan=1)



button_del=Button(root, text="DELETE_TASK", padx=5, pady=5, command=deletetask)

button_del.grid(row=2, column=2)



button_done=Button(root, text="MARK AS DONE", padx=10, pady=10, command= markdone, bg="light blue")

button_done.grid(row=3, column=0)



root.mainloop()