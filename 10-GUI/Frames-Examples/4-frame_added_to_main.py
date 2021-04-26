 
import tkinter as tk
mainwindow = tk.Tk()
mainwindow.geometry("300x400")
 
myFrameBob = tk.Frame(mainwindow, bg="green")
myFrameBob.pack()
#myFrameBob.place(x=0, y=0, relwidth=1, relheight=1)
 
# myButt1 = tk.Button(myFrameBob, bg='orange', text='button one')
# myButt1.pack()
 
mainwindow.mainloop()
