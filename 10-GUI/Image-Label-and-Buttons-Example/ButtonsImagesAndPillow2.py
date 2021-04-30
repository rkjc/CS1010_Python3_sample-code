 
from tkinter import *
from PIL import ImageTk, Image

# for more complicated image manipulation checkout the PIL pillow library
# https://github.com/python-pillow/Pillow

root = Tk()
root.geometry("600x600")
# root.columnconfigure(0, minsize=100)
# root.columnconfigure(1, minsize=200)

img01_altPhoto = None

def doButton1():
    label_1.config(image = space_pic_resize_2)
    label_1.tkraise()
    root.after(1000, revert_all)

def doButton2():
    pass

def revert_all():
    label_1.config(image="")


#images have to be .png, .jpg does not work.

img01_org = Image.open("Space_Woman.png")
img01_photo = ImageTk.PhotoImage(img01_org)
img01_width = img01_photo.width()
img01_height = img01_photo.height()


scale_1 = 0.2
img01_altSizeImage = img01_org.resize((int(img01_width * scale_1), int(img01_height * scale_1)))
img01_altPhoto = ImageTk.PhotoImage(img01_altSizeImage)

space_scale_2 = 600 / img01_width
space_img_resize_2 = img01_org.resize((int(img01_width * space_scale_2), int(img01_height * space_scale_2)))
space_pic_resize_2 = ImageTk.PhotoImage(space_img_resize_2)


label_1 = Label(root)
label_1.place(x=0, y=0)


MyButton1 = Button(root, text="b1", image=img01_altPhoto, bg="cyan", command = doButton1)
MyButton1.grid(row=0, column=0)

MyButton2 = Button(root, text="b2", image=kat_pic_resize_1, bg="cyan", command = doButton2)
MyButton2.grid(row=0, column=1)

root.mainloop()


# https://appdividend.com/2020/06/19/how-to-resize-image-in-python-using-pillow-example/

