# Used to test code before entered into final  piece of code. Used so I don't need to
# Change all my code to test one function
# Import Module
from tkinter import *

# Create Object
root = Tk()

# Set geometry
root.geometry('400x500')

# Information List
datas = []

# Add Information
def add():
    global datas
    datas.append([Name.get(), ItemHired.get(), ItemQuantity.get(), ReceiptNumber.get()])
    update_book()

# View Information
def view(*args):
    selection = select.curselection()
    if selection:
        index = int(selection[0])
        Name.set(datas[index][0])
        ItemHired.set(datas[index][1])
        ItemQuantity.set(datas[index][2])
        ReceiptNumber.set(datas[index][3])

# Delete Information
def delete():
    selection = select.curselection()
    if selection:
        index = int(selection[0])
        del datas[index]
        update_book()

# Update Information
def update_book():
    select.delete(0, END)
    for data in datas:
        select.insert(END, data)

# Create a new Toplevel window
listbox_window = Toplevel(root)
listbox_window.title("List Box")
listbox_window.withdraw()  # Hide the window initially

scroll_bar = Scrollbar(listbox_window, orient=VERTICAL)
select = Listbox(listbox_window, yscrollcommand=scroll_bar.set, height=10)
scroll_bar.config(command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.pack(fill=BOTH, expand=True)

select.bind('<<ListboxSelect>>', view)  # Bind view function to selection event

# Open the List Box Window
def open_listbox_window():
    update_book()  # Update the listbox with the latest data
    listbox_window.deiconify()  # Show the List Box Window

# Add Buttons, Label
Name = StringVar()
ItemHired = StringVar()
ItemQuantity = IntVar()
ReceiptNumber = StringVar()

frame = Frame(root)
frame.pack(pady=10)

frame1 = Frame(root)
frame1.pack()

frame2 = Frame(root)
frame2.pack(pady=10)

frame3 = Frame(root)
frame3.pack()

Label(frame, text='Name').grid(row=0, column=0, sticky=W)
Entry(frame, textvariable=Name, width=50).grid(row=0, column=1)

Label(frame1, text='Item Hired').grid(row=0, column=0, sticky=W)
Entry(frame1, textvariable=ItemHired, width=50).grid(row=0, column=1)

Label(frame2, text='Item Quantity').grid(row=0, column=0, sticky=W)
Entry(frame2, textvariable=ItemQuantity, width=37).grid(row=0, column=1)

Label(frame3, text='Receipt Number').grid(row=0, column=0, sticky=W)
Entry(frame3, textvariable=ReceiptNumber, width=37).grid(row=0, column=1)

Button(root, text="Add", command=add).place(x=100, y=370)
Button(root, text="Delete", command=delete).place(x=100, y=410)
Button(root, text="View All", command=open_listbox_window).place(x=100, y=450)  # Button to open List Box Window

# Initial population of Listbox
update_book()

# Execute Tkinter
root.mainloop()
