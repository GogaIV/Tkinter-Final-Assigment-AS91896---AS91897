# Used to test code before entered into final  piece of code. Used so I don't need to
# Change all my code to test one function
# Import Module
from tkinter import *
import base64, zlib
import tempfile
from tkinter import messagebox
import tkinter.font as tkfont

# Making a transparent window icon instead of a feather
ICON = zlib.decompress(
    base64.b64decode(
        "eJxjYGAEQgEBBiDJwZDBy"
        "sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc="
    )
)
_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, "wb") as icon_file:
    icon_file.write(ICON)

# Creating window for program
root = Tk()
# Icon bitmap sets the feather to whatever file I want it to be , in this case its transparent
root.iconbitmap(default=ICON_PATH)
root.minsize(height=300, width=400)
root.title("Main Menu")
canvas = Canvas(root)


# Making the program look better with rounded corners
def round_rectangle_border(x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1 + radius,
        y1,
        x1 + radius,
        y1,
        x2 - radius,
        y1,
        x2 - radius,
        y1,
        x2,
        y1,
        x2,
        y1 + radius,
        x2,
        y1 + radius,
        x2,
        y2 - radius,
        x2,
        y2 - radius,
        x2,
        y2,
        x2 - radius,
        y2,
        x2 - radius,
        y2,
        x1 + radius,
        y2,
        x1 + radius,
        y2,
        x1,
        y2,
        x1,
        y2 - radius,
        x1,
        y2 - radius,
        x1,
        y1 + radius,
        x1,
        y1 + radius,
        x1,
        y1,
    ]

    return canvas.create_polygon(points, **kwargs, smooth=True)


my_rectangle = round_rectangle_border(50, 50, 150, 100, radius=20, fill="blue")


# Information List
datalist = []


# Add Information
def add():
    global datalist
    datalist.append([name.get(), recieptnum.get(), itemquantity.get()])
    update_book()


# Delete Information
def delete():
    del datalist[int(select.curselection()[0])]
    update_book()


# Update Information
def update_book():
    select.delete(0, END)
    for n, p, a in datalist:
        select.insert(END, n, p, a)


# Add Buttons, Label, ListBox
name = StringVar()
itemhired = StringVar()
itemquantity = StringVar()
recieptnum = StringVar()

frame1 = Frame()
frame1.grid(column=1, row=1)

frame2 = Frame()
frame2.grid(column=1, row=2)

namelabel = Label(frame1, text="Name").grid(column=1, row=1, sticky=W)
Name = Entry(frame1, textvariable=name).grid(column=2, row=1)

itemhiredlabel = Label(frame1, text="Item").grid(column=1, row=2, sticky=W)
itemhired = Entry(frame1, textvariable=itemhired).grid(column=2, row=2)

itemquantitylabel = Label(frame1, text="Item Quantity").grid(column=1, row=3, sticky=W)
itemquantity = Entry(frame1, textvariable=itemquantity)
itemquantity.grid(column=2, row=3)

reciptnumlabel = Label(frame1, text="Reciept Number").grid(column=1, row=4)
recieptnum = Entry(frame1, textvariable=recieptnum)
recieptnum.grid(column=2, row=4)

Button(frame1, text="Add", command=add).grid(column=1, row=5, sticky=W)
Button(frame1, text="Delete", command=delete).grid(column=1, row=5, sticky=E)


scroll_bar = Scrollbar(frame2, orient=VERTICAL)
select = Listbox(frame2, yscrollcommand=scroll_bar.set, height=14)
scroll_bar.config(command=select.yview)
scroll_bar.grid(column=3, row=1)
select.grid(column=2, row=1)


# Execute Tkinter
root.mainloop()
