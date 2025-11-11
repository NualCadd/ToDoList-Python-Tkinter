
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from datetime import datetime
time = datetime.now().strftime("%d/%m/%Y")
task_x = 400
task_y = 300
count = 0
task_list =[]
label_list = []
checkbox_list = []
def openwindow():
    global window, secondwindow, progress
    window.withdraw()
    secondwindow = Toplevel(window)
    secondwindow.geometry(f"900x700+{window.winfo_x()}+{window.winfo_y()}")
    secondwindow.title("To-Do List")
    secondwindow.resizable(False, False)
    secondwindow.config(bg="#93c47d")
    secondbackground = Label(secondwindow, bg="#93c47d")
    secondbackground.place(x=0, y=0, relwidth=1, relheight=1)

    img = Image.open("card.png")
    img = img.resize((300,400), Image.LANCZOS)
    img = img.convert("RGBA")
    card = ImageTk.PhotoImage(img)
    cardlabel = Label(secondwindow,image=card,
                      bd=0)
    cardlabel.place(x=50,y=50)

    img1= Image.open("calendar.png")
    img1 = img1.resize((250,250), Image.LANCZOS)
    img1 = img1.convert("RGBA")
    calendar = ImageTk.PhotoImage(img1)
    calendar_label = Label(secondwindow, image=calendar,
                           bd=0)
    calendar_label.place(x=50,y=450)

    time_label = Label(secondwindow,text=time,
                       font=("Comic Sans MS", 25, "bold"),
                         bg="#93c47d", fg="white")
    time_label.place(x=310,y=600)



    progress = ttk.Progressbar(secondwindow, orient=HORIZONTAL, 
                               length=300, 
                               mode='determinate',
                               style = "Custom.Horizontal.TProgressbar",
                               value = 0,
                               )
    progress.place(x=400, y=100)

    progresstext = Label(secondwindow, text = "Your Progress",
                         font=("Comic Sans MS", 25, "bold"),
                         bg="#93c47d", fg="white")
    progresstext.place(x=400,y=30)

    addbutton = Button(secondwindow, text="Add Task",
                       font=("Comic Sans MS", 20,"bold"),
                       bg="#73a05e", fg="white",
                       relief="flat",
                       activebackground="#73a05e",
                       activeforeground="white",
                       command=add_task)
    addbutton.place(x=400,y=150)

    removebutton = Button(secondwindow,text="Remove Task",
                          font=("Comic Sans MS", 20,"bold"),
                          bg="#73a05e", fg="white",
                          relief="flat",
                          activebackground="#73a05e",
                          activeforeground="white",
                          command=delete_task)
    removebutton.place(x=600,y=150)

def add_task():
    global box, submitbutton
    box = Entry(secondwindow,width=20, font=("Comic Sans MS", 20,"bold"))
    box.place(x=400,y=250)
    submitbutton = Button(secondwindow,text="Submit",
                          font=("Comic Sans MS", 20,"bold"),
                          bg="#73a05e", fg="white",
                          relief="flat",
                          activebackground="#73a05e",
                          activeforeground="white",
                          command=submit)
    submitbutton.place(x=750,y=240)

def submit():
    global count,name,task_list
    
    count+=1
    name = box.get()
    task_list.append(name)
    show()
    
    

def done():
    global annoucement
    percentage = 100 / count
    progress["value"] += percentage
    if progress["value"] >= 100:
        annoucement = Label(secondwindow, text="All tasks completed!!",
                            font=("Comic Sans MS", 14, "bold"),
                            bg="#93c47d", fg="white")
        annoucement.place(x=700,y=90)     

def delete_task():
    global task_list, label_list, checkbox_list,count
    label_list[count-1].destroy()
    checkbox_list[count-1].destroy()
    task_list.pop()
    label_list.pop()
    checkbox_list.pop()
    count -= 1
    show()


def show():
    global task_x, task_y,task_list,checkbox_list,label_list
    task_x = 400
    task_y = 300
    
    
    for task_label in label_list:
        task_label.destroy()
    for checkbox in checkbox_list:
        checkbox.destroy()
    label_list.clear()
    checkbox_list.clear()


    for task in task_list:
        task_label = Label(secondwindow,text=task,
                           font=("Comic Sans MS", 20, "bold"),
                            bg="#93c47d", fg="black")
        task_label.place(x=task_x, y=task_y)
        checkbox  = Checkbutton(secondwindow,
                               bg="#93c47d",
                               activebackground="#73a05e",
                               command=done)
        checkbox.place(x=task_x-30,y=task_y+10)
        task_y += 50
        label_list.append(task_label)
        checkbox_list.append(checkbox)
    box.destroy()
    submitbutton.destroy()
    



    
window = Tk()
window.title("To-Do List")
window.geometry("900x700+50+50")
window.resizable(False, False)
window.config(bg="#93c47d")

#style 
style = ttk.Style()
style.theme_use("clam")
style.configure("Custom.Horizontal.TProgressbar",
                troughcolor = "white",
                background = "#44624a",
                thickness = 1000,
                )


img = Image.open("download.jpg")
name = Label(window,text="To-Do List", font=("Comic Sans MS", 40, "bold"),bg="#93c47d",fg="white")
name.pack(pady=20)
draw = Image.open("draw.png")
draw = draw.resize((800,400), Image.LANCZOS)
draw = draw.convert("RGBA")
draws = ImageTk.PhotoImage(draw)
drawplace = Label(window, image=draws,
                  bd=0)
drawplace.pack()


button = Image.open("button.png")
button = button.resize((150,50), Image.NEAREST)
buttonimage = ImageTk.PhotoImage(button)
buttonbackground = Label(window,image=buttonimage,
                         bd=0,
                         highlightthickness=0)
buttonbackground.place(x=450,y=600,anchor=CENTER)


startbutton = Button(window,text="Start", 
                     font=("Comic Sans MS", 20, "bold"), 
                     bg="#358045", fg="white",
                     command=openwindow,
                     relief="flat",
                     activebackground="#358045",
                     activeforeground="white",
                    )
startbutton.place(x=450, y=600,width=140,height=40,anchor=CENTER)



window.mainloop()

