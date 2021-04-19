import tkinter as tk

groot = tk.Tk()
groot.geometry("300x200")

def func_one():
    str_var1 = E1.get()
    str_var1 = "Hi there " + str_var1
    L2.configure(text=str_var1)


L1 = tk.Label(groot, text = "Enter User Name")
L1.pack()

E1 = tk.Entry(groot)
E1.pack()

B1 = tk.Button(groot, text="post the entry", command=func_one)
B1.pack()

L2 = tk.Label(groot, text = "---------------")
L2.pack()

groot.mainloop()