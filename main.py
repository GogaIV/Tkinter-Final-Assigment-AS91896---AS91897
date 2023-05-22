from tkinter import *
from tkcalendar import *
import base64
import zlib
import tempfile
from tkinter import messagebox
import tkinter.font as tkfont
import sqlite3


# Making a clear icon instead of feather on program window
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
root.iconbitmap(default=ICON_PATH)
root.minsize(height=120, width=170)
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


# Creating the main menu
def Menu():
    # Making record keeper page
    def recordpage():
        # Destorying previous page elemnts
        menubutton_1.destroy()
        label_name.destroy()
        root.title("Record Manager")
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
        global query_button

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

        # Making databse
        conn = sqlite3.connect("partyhires.db")

        # Creating a cursor for databse
        c = conn.cursor()

        # c.execute(
        #         """CREATE TABLE partyhires (
        #         customer_name_label text,
        #         item_hired_label text,
        #         item_quantity_label interger,
        #         reciept_num_label text
        #         )"""
        # )

        # Adding enter button to accept the values enetered

        def enter():
            # Checks if item quantity inputted is a number
            # try:
            #     global item_quantity_input_interger
            #     item_quantity_input_interger = int(item_quantity_input.get())
            # except ValueError:
            #     messagebox.showerror("Error", "Please enter number!")

            # # Then checks if item quantity inputted is a number within 500 otherwise becomes invalid
            # if item_quantity_input_interger > 500:
            #     messagebox.showerror("Error", "Please enter a number within 500!")
            #     item_quantity_input = " "

            # Making database
            conn = sqlite3.connect("partyhires.db")

            # Creating a cursor for databse
            c = conn.cursor()

            # Creating databse
            c.execute(
                "INSERT INTO partyhires VALUES (:customer_name_input, :item_hired_input, :item_quantity_input, :reciept_num_input)",
                {
                    "customer_name_input": customer_name_input.get(),
                    "item_hired_input": item_hired_input.get(),
                    "item_quantity_input": item_quantity_input.get(),
                    "reciept_num_input": reciept_num_input.get(),
                },
            )

            # Commiting the changes to database
            conn.commit()

            # Closing the connectin for when user presses X
            conn.close()

            customer_name_input.delete(0, END)
            item_hired_input.delete(0, END)
            item_quantity_input.delete(0, END)
            reciept_num_input.delete(0, END)

        # Create function for query button
        def query():
            # Making database
            conn = sqlite3.connect("partyhires.db")

            # Creating a cursor for databse
            c = conn.cursor()

            # Querying databse
            c.execute("SELECT *, oid FROM partyhires")
            records = c.fetchall()
            print(records)

            # Loop through records
            print_records = ""
            for record in records:
                print_records +=  str(record[0]) + " " + str(record[6]) + "\n"

            query_label = Label(root, text=print_records)
            query_label.grid(row=6, column=1)

            print_records = ""
            for record in records:
                print_records += record[1] + "\n"

            query_label2 = Label(root, text=print_records)
            query_label2.grid(row=6, column=2)

            for record in records:
                print_records += str(record[2]) + "\n"

            query_label3 = Label(root, text=print_records)
            query_label3.grid(row=6, column=3)

            for record in records:
                print_records += str(record[3]) + "\n"

            query_label4 = Label(root, text=print_records)
            query_label4.grid(row=6, column=4)

            # Commiting the changes to database
            conn.commit()

            # Closing the connectin for when user presses X
            conn.close()

        enterbutton = Button(root, text="Enter", command=enter)
        enterbutton.grid(column=1, row=5)

        # Creating a query button
        query_button = Button(root, text="Show Records", command=query)
        query_button.grid(column=3, row=1, sticky=W)

        # Adding back button for record keeping page
        global button_2
        button_2 = Button(
            root, text="<--Menu", width="7", command=back, activebackground="red"
        )
        button_2.grid(column=2, row=1, sticky=E)

        # Making a back button that can be used on all pages.

    def back():
        root.minsize(height=120, width=170)
        root.title("Main Menu")
        Menu()

        # removing the back button
        button_2.destroy()

        # Removing the other assests, buttons and labels
        customer_name_label.destroy()
        item_hired_label.destroy()
        enterbutton.destroy()
        item_quantity_label.destroy()
        reciept_num_label.destroy()
        customer_name_input.destroy()
        item_hired_input.destroy()
        item_quantity_input.destroy()
        reciept_num_input.destroy()
        query_button.destroy()

    # Labeling the main menu
    label_name = Label(
        root, text="Party Hire Store Record Keeper", font=(25), padx=8, pady=5
    )
    label_name.grid(column=2, row=1)

    # Making buttons to seperate
    menubutton_1 = Button(
        root, text="Record Manager", command=recordpage, activebackground="white"
    )
    menubutton_1.grid(column=2, row=3)

    menubutton_2


Menu()
root.mainloop()
