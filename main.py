from tkinter import *
from tkcalendar import *
import base64, zlib
import tempfile
from tkinter import messagebox
import tkinter.font as tkfont
import sqlite3


# Making a clear icon instead of feather on program window
# ICON = zlib.decompress(
#     base64.b64encode(
#         "eJxjYGAEQgEBBiDJwZDBy"
#         "sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc="
#     )
# )

# _, ICON_PATH = tempfile.mkstemp()
# with open(ICON_PATH, "wb") as icon_file:
#     icon_file.write(ICON)

# Creating window for program
root = Tk()
root.minsize(height=200, width=170)
root.title("Party Hire Store Record Keeper")
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


# Creating the main menu
def Menu():
    # Making record keeper page
    def recordpage():
        root.minsize(height=200, width=170)

        # Making everything global to be used on the back function
        global customer_name_label
        global item_hired_label
        global item_quantity_label
        global reciept_num_label
        global customer_name_input
        global item_quantity_input
        global reciept_num_input
        global item_hired_input
        global enterbutton

        # Labels for the input boxes
        customer_name_label = Label(root, text="Customer Name")
        customer_name_label.grid(column=1, row=2)
        item_hired_label = Label(root, text="Hired Item")
        item_hired_label.grid(column=2, row=2)
        item_quantity_label = Label(root, text="Item Quantity")
        item_quantity_label.grid(column=3, row=2)
        reciept_num_label = Label(root, text="Reciept Number")
        reciept_num_label.grid(column=4, row=2)

        # Input boxes
        customer_name_input = Entry(root)
        customer_name_input.grid(column=1, row=3)
        item_hired_input = Entry(root)
        item_hired_input.grid(column=2, row=3)
        item_quantity_input = Entry(root)
        item_quantity_input.grid(column=3, row=3)
        reciept_num_input = Entry(root)
        reciept_num_input.grid(column=4, row=3)

        # Adding enter button to accept the values enetered
        def enter():
            # Making message boxes for incorrect input values

            # Checks if item quantity inputted is a number
            try:
                item_quantity_input_interger = int(item_quantity_input.get())
            except ValueError:
                messagebox.showerror("Error", "Please enter number!")

            # Then checks if item quantity inputted is a number within 500 otherwise becomes invalid
            if item_quantity_input_interger > 500:
                messagebox.showerror("Error", "Please enter a number within 500!")
                item_quantity_input_interger = " "

            # Making all future values into global to be used in dictionary creation
            global rni
            global cni
            global ihi
            global iqi
            cni = customer_name_input.get()
            ihi = item_hired_input.get()
            iqi = item_quantity_input_interger
            rni = reciept_num_input.get()
            print(cni, ihi, iqi, rni)

        enterbutton = Button(root, text="Enter", command=enter)
        enterbutton.grid(column=1, row=5)

        # Destorying previous page elemnts
        menubutton_1.destroy()
        menubutton_2.destroy()
        label_1.destroy()
        emptylabel1.destroy()
        emptylabel2.destroy()

        # Adding back button for record keeping page
        global button_2
        button_2 = Button(
            root, text="<--Menu", width="7", command=back, activebackground="red"
        )
        button_2.grid(column=1, row=1, sticky=W)


    # Making Record Viewing page
    def viewrecordspage():
        root.minsize(height=200, width=170)
        label_1.destroy()
        menubutton_1.destroy()
        menubutton_2.destroy()
        emptylabel1.destroy()
        emptylabel2.destroy()

        # Making everything global to be used on the back function
        global customer_name_label
        global item_hired_label
        global item_quantity_label
        global reciept_num_label

        # Labels for the grid boxes
        customer_name_label = Label(root, text="Customer Name")
        customer_name_label.grid(column=1, row=2)
        item_hired_label = Label(root, text="Hired Item")
        item_hired_label.grid(column=2, row=2)
        item_quantity_label = Label(root, text="Item Quantity")
        item_quantity_label.grid(column=3, row=2)
        reciept_num_label = Label(root, text="Reciept Number")
        reciept_num_label.grid(column=4, row=2)

        #Making each variable unique to place into grid boxes
            

        # Adding back button for record viewing page
        global button_2
        button_2 = Button(
            root, text="<--Menu", width="7", command=back, activebackground="red"
        )
        button_2.grid(column=1, row=1, sticky=W)


        # Making a back button that can be used on all pages.

    def back():
        root.minsize(height=200, width=170)
        root.title("Party Hire Store Record Keeper")
        Menu()

        # removing the back button
        button_2.destroy()

        # Removing the other assests,  buttons and labels
        customer_name_label.destroy()
        item_hired_label.destroy()
        enterbutton.destroy()
        item_quantity_label.destroy()
        reciept_num_label.destroy()
        customer_name_input.destroy()
        item_hired_input.destroy()
        item_quantity_input.destroy()
        reciept_num_input.destroy()

    # Labeling the main menu
    label_1 = Label(root, text="Main Menu", font=(25))
    label_1.grid(column=2, row=1)

    # Making buttons to seperate
    menubutton_1 = Button(
        root, text="Add a Record", command=recordpage, activebackground="white"
    )
    menubutton_1.grid(column=2, row=2)
    menubutton_2 = Button(
        root, text="View Records", command=viewrecordspage, activebackground="white"
    )
    menubutton_2.grid(column=2, row=3)

    # Adding a spacing between sides and menu
    emptylabel1 = Label(root, text="", padx=20)
    emptylabel1.grid(column=1, row=2)
    emptylabel2 = Label(root, text="", padx=20)
    emptylabel2.grid(column=3, row=2)


Menu()
root.mainloop()
