from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("alert","stop! virus found.")
button=Button(root,text="Scan for virus",command=msg)
button.place(x=70,y=20)
root.mainloop()    