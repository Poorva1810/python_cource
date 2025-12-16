import tkinter as tik
window =tik.Tk()
for i in range(4):
    for j in range(3):
        frame =tik.Frame(
            master=window,
            relief=tik.RAISED,
            borderwidth=12
        )
        frame.grid(row=i,column=j,padx=10,pady=10)
        label=tik.Label(master=frame, text=f"Row{i}\nColumn{j}")
        label.pack()
window.mainloop()        