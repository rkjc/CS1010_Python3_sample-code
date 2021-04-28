import tkinter

# for more complicated image manipulation checkout the PIL pillow library
# https://github.com/python-pillow/Pillow

root = tkinter.Tk()
root.columnconfigure(0, minsize=100)
root.columnconfigure(1, minsize=200)

def doButton1():
    label_1.config(image=img1)
    label_2.config(text="Image One")

def doButton2():
    label_1.config(image=img2)
    label_2.config(text="Image Two")

def doButton3():
    label_1.config(image=img3)
    label_2.config(text="Image Three")


#images have to be .png, .jpg does not work.
img1 = tkinter.PhotoImage(file="Space_Woman.png")
im1a = img1.subsample(5)

img2 = tkinter.PhotoImage(file="vigo_700.png")
im2a = img2.subsample(4)

img3 = tkinter.PhotoImage(file="Enterprise_700.png")
im3a = img3.subsample(4)

label_1 = tkinter.Label(root, text="images")
label_1.grid(row=1, rowspan=3, column=1)

label_2 = tkinter.Label(root, text="select an image")
label_2.grid(row=0, column=1)


MyButton1 = tkinter.Button(root, image=im1a, text="b1", bg="blue",width=100, height=100, command = lambda: doButton1())
MyButton1.grid(row=1, column=0)

MyButton1 = tkinter.Button(root, image=im2a, text="b2", bg="blue",width=100, height=100, command = lambda: doButton2())
MyButton1.grid(row=2, column=0)

MyButton1 = tkinter.Button(root, image=im3a, text="b3", bg="blue",width=100, height=100, command = lambda: doButton3())
MyButton1.grid(row=3, column=0)


root.mainloop()
