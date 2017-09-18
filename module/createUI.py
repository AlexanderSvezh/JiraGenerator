from tkinter import *
import requests

login=<login>
password=<pass>
# auth=(login,password)

def click():
    if var.get()==1:
        logline.delete(1.0,END)
        logline.insert(END,"(new task)")
        ent01.delete(0,END)
        ent01.insert(END,"(new task)")
    if var.get()==2:
        logline.delete(1.0,END)
        logline.insert(END,"(subtask)")
        ent01.delete(0,END)
        ent01.insert(END,"(subtask)")

def click_default():
    ent1.delete(0,END)
    ent1.insert(END, 'LOAD')
    ent2.delete(0,END)
    ent2.insert(END, u'Да')
    ent3.delete(0,END)
    ent3.insert(END, u'НТ1-N1326/17')
    ent4.delete(0,END)
    ent4.insert(END, 'major')
    ent5.delete(0,END)
    ent5.insert(END, 'PDP')
    ent6.delete(0,END)
    ent6.insert(END, login)

def hide_me(event):
    event.widget.pack_forget()

def exit():
    root.destroy()

root=Tk()
var=IntVar()
var.set(1)

root.title('Генератор Жира!')

frame1=Frame(root,width=850,height=300)

lab = Label(frame1, text="Choose task for enter timeworks:", font="Arial 11")
# lab.pack(side=TOP)

rb1=Radiobutton(frame1,text='New Task',
                     padx = 45,
                     variable=var,
                     value=1,
                     indicatoron=0)
rb2=Radiobutton(frame1,text='Sub-Task',
                     padx = 45,
                     variable=var,
                     value=2,
                     indicatoron=0)

create_button = Button(frame1, text=u"Create", padx=50, command=click)
default_button = Button(frame1, text=u"Default", padx=40, command=click_default)
exitbutton=Button(frame1,text='Exit', padx=30, command=exit)
logline = Text(root,width=20,height=3,font="12",wrap=WORD)

ent01 = Entry(frame1, width=20)
ent02 = Entry(frame1, width=20)
ent02.insert(END, '(title)')
ent03 = Entry(frame1, width=20)
ent03.insert(END, '(comment)')
ent1 = Entry(frame1, width=20)
ent1.insert(END, 'project')
ent2 = Entry(frame1, width=20)
ent2.insert(END, 'outsource')
ent3 = Entry(frame1, width=20)
ent3.insert(END, 'specification')
ent4 = Entry(frame1, width=20)
ent4.insert(END, 'priority')
ent5 = Entry(frame1, width=20)
ent5.insert(END, 'component')
ent6 = Entry(frame1, width=20)
ent6.insert(END, 'assignee')

ent_time1 = Entry(frame1, width=20)
ent_time1.insert(END, '(work comment)')
ent_time2 = Entry(frame1, width=20)
ent_time2.insert(END, '(work date)')
ent_time3 = Entry(frame1, width=20)
ent_time3.insert(END, '(spent time)')

frame1.pack()
rb1.place(relx=0.05,rely=0.05)
rb2.place(relx=0.05,rely=0.12)

create_button.place(relx=0.05,rely=0.35)
default_button.place(relx=0.3,rely=0.5)

logline.place(relx=0.05,rely=0.6)
exitbutton.place(relx=0.75,rely=0.8)

ent01.place(relx=0.3,rely=0.05)
ent02.place(relx=0.3,rely=0.25)
ent03.place(relx=0.3,rely=0.35)
ent1.place(relx=0.5,rely=0.05)
ent2.place(relx=0.5,rely=0.15)
ent3.place(relx=0.5,rely=0.25)
ent4.place(relx=0.5,rely=0.35)
ent5.place(relx=0.5,rely=0.45)
ent6.place(relx=0.5,rely=0.55)

ent_time1.place(relx=0.75,rely=0.15)
ent_time2.place(relx=0.75,rely=0.25)
ent_time3.place(relx=0.75,rely=0.35)

root.mainloop()
