import tkinter
import tkinter.messagebox
import random

root = tkinter.Tk()


root.configure(bg="white")

root.title("To-Do")


root.geometry("400x500")


tasks=[]


def update_listbox():
    
    clear_listbox()

    for task in tasks:
        lb_tasks.insert("end",task)
        
def clear_listbox():
    lb_tasks.delete(0,"end")

def add_task():
    
    task = txt_input.get()
    
    if task != "":
        
        tasks.append(task)
        
        update_listbox()
    else:
        tkinter.messagebox.showwarning("Warning", "You need to enter the task")
    txt_input.delete(0,"end")

def delete_all():
    confirmed = tkinter.messagebox.askyesno("Please Confirm", "Do you really want to delete all ?")
    if confirmed == True:
        
        global tasks
        
        tasks = []
        update_listbox()
    else:
        pass

    
def delete_one():
    
    task = lb_tasks.get("active")
    
    if task in tasks:
        tasks.remove(task)
    
    update_listbox()

def sort_asc():
    
    tasks.sort()
    
    update_listbox()

def sort_desc():

    tasks.sort()

    tasks.reverse()
    
    update_listbox()

def choose_random():
    
    task = random.choice(tasks)
    
    lbl_display["text"] = task

def show_number_of_tasks():
    
    number_of_tasks = len(tasks)
    
    msg = "Number of tasks : %s" %number_of_tasks
    
    lbl_display["text"] = msg


lbl_title = tkinter.Label(root, text="To-Do-List", bg="white")
lbl_title.grid(row=0,column=0, padx=5, pady=2)

lbl_display = tkinter.Label(root, text="", bg="white")
lbl_display.grid(row=0,column=1, padx=5, pady=2)

txt_input = tkinter.Entry(root, width=15, border="2px solid black")
txt_input.grid(row=1,column=1, padx=5, pady=2)

btn_add_task = tkinter.Button(root, text="Add Task", fg="white", bg="purple", command=add_task, width=20)
btn_add_task.grid(row=1,column=0, padx=5, pady=2)

btn_del_all = tkinter.Button(root, text="Delete All", fg="white", bg="maroon", command=delete_all, width=20)
btn_del_all.grid(row=2,column=0, padx=5, pady=2)

btn_del_one = tkinter.Button(root, text="Delete", fg="white", bg="olive", command=delete_one, width=20)
btn_del_one.grid(row=3,column=0, padx=5, pady=2)

btn_sort_asc = tkinter.Button(root, text="Sort (ASC)", fg="black", bg="lightblue", command=sort_asc, width=20)
btn_sort_asc.grid(row=4,column=0, padx=5, pady=2)

btn_sort_desc = tkinter.Button(root, text="Sort (DESC)", fg="white", bg="olive", command=sort_desc, width=20)
btn_sort_desc.grid(row=5,column=0, padx=5, pady=2)

btn_choose_random = tkinter.Button(root, text="Choose Random", fg="white", bg="maroon", command=choose_random, width=20)
btn_choose_random.grid(row=6,column=0, padx=5, pady=2)

btn_number_of_tasks = tkinter.Button(root, text="Number of Tasks", fg="black", bg="lightblue", command=show_number_of_tasks, width=20)
btn_number_of_tasks.grid(row=7,column=0, padx=5, pady=2)

btn_exit = tkinter.Button(root, text="Exit", fg="black", bg="red", command=quit, width=20)
btn_exit.grid(row=8,column=0, padx=5, pady=2)

lb_tasks  = tkinter.Listbox(root, width=25, bg="#f4f4f4", border="2px solid black")
lb_tasks.grid(row=2,column=1,rowspan=7, padx=10, pady=10)


root.mainloop()