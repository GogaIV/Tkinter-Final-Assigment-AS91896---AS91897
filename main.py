import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox
import base64, zlib
import tempfile

# Making a transparent window icon instead of a feather
ICON = zlib.decompress(
    base64.b64decode(
        "eJxjYGAEQgEBBiDJwZDBy"
        "sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc="
    )
)

# Makes a temp file to use as the window icon.
_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, "wb") as icon_file:
    icon_file.write(ICON)


# Creating record viewiing page (for the database)
def record_viewer():
    # Clear the existing labels in the display window
    #winfo_children destroys all existing varibales.
    for widget in record_viewer_window.winfo_children():
        widget.destroy()

    # Connect to the database
    connection = sqlite3.connect("userdata.db")
    # Sets the usage of the cursor
    cursor = connection.cursor()
    # Able to select input from databse
    cursor.execute("SELECT rowid, * FROM users")
    # When clicked fetches all inputs on that line
    users = cursor.fetchall()
    # closes the connection and after window closure
    connection.close()

    # Creates labels to define each column
    name_label = tk.Label(
        record_viewer_window, text="Name", font=("Helvetica", 12, "bold")
    )
    name_label.grid(row=0, column=0, padx=5, pady=5)
    item_hired_label = tk.Label(
        record_viewer_window, text="Item Hired", font=("Helvetica", 12, "bold")
    )
    item_hired_label.grid(row=0, column=1, padx=5, pady=5)
    item_quantity_label = tk.Label(
        record_viewer_window, text="Item Quantity", font=("Helvetica", 12, "bold")
    )
    item_quantity_label.grid(row=0, column=2, padx=5, pady=5)
    receipt_number_label = tk.Label(
        record_viewer_window, text="Receipt Number", font=("Helvetica", 12, "bold")
    )
    receipt_number_label.grid(row=0, column=3, padx=5, pady=5)

    # Display the inputs in a grid by selecting first variable and placing it in a column underneath each label
    # Also adds a delete button next to each input
    for i, user in enumerate(users):
        party_hirer_info = user[0]
        name_label = tk.Label(record_viewer_window, text=user[1])
        name_label.grid(row=i + 1, column=0, padx=5, pady=5)
        item_hired_label = tk.Label(record_viewer_window, text=user[2])
        item_hired_label.grid(row=i + 1, column=1, padx=5, pady=5)
        item_quantity_label = tk.Label(record_viewer_window, text=user[3])
        item_quantity_label.grid(row=i + 1, column=2, padx=5, pady=5)
        receipt_number_label = tk.Label(record_viewer_window, text=user[4])
        receipt_number_label.grid(row=i + 1, column=3, padx=5, pady=5)
        delete_button = tk.Button(
            record_viewer_window,
            text="Delete",
            command=lambda id=party_hirer_info: delete_entry(id),
        )
        delete_button.grid(row=i + 1, column=4, padx=5, pady=5)


# Pulls each input on enter and changes their varibale name
def enter():
    name = name_entry.get()
    item_hired = item_hired_entry.get()
    item_quantity = item_quantity_entry.get()
    receipt_number = receipt_number_entry.get()

    # Checks if item_quantity is a digit then checks if it is within the accepted range
    if not item_quantity.isdigit() or not (1 <= int(item_quantity) <= 500):
        messagebox.showerror(
            "Invalid Input", "Item Quantity must be a number between 1 and 500."
        )
        return

    # checks if receipt_number as a digit else it shows a error box.
    if not receipt_number.isdigit():
        messagebox.showerror("Invalid Input", "Receipt Number must be a digit.")
        return
    
    #checks that all input boxes have inputs
    if name == "" :
        messagebox.showerror("Invalid Input", "Name cannot be empty.")
        return 
    
    if item_hired == "" :
        messagebox.showerror("Invalid Input", "Item Hired cannot be empty.")
        return
    

    # Add "rcn" prefix to the receipt_number
    # RCN stands for recipet number
    receipt_number = "RCN" + receipt_number

    # Save the inputs to a database
    connection = sqlite3.connect("userdata.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (name TEXT, item_hired TEXT, item_quantity INTEGER, receipt_number INTEGER)"
    )
    cursor.execute(
        "INSERT INTO users VALUES (?, ?, ?, ?)",
        (name, item_hired, item_quantity, receipt_number),
    )
    connection.commit()
    connection.close()
    
    # Clear the entry fields after saving
    name_entry.delete(0, tk.END)
    item_hired_entry.delete(0, tk.END)
    item_quantity_entry.delete(0, tk.END)
    receipt_number_entry.delete(0, tk.END)

    # Refresh the display window to display new inputs
    record_viewer()


def delete_entry(party_hirer_info):
    # Delete the selected entry from the database using a cursor
    connection = sqlite3.connect("userdata.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE rowid=?", (party_hirer_info,))
    connection.commit()
    connection.close()

    # Refresh the display window after deleting the entry
    record_viewer()


# Creating the window
root = tk.Tk()
root.iconbitmap(default=ICON_PATH)
root.title("Julie's Party Hire Record Keeper")
root.geometry("250x250")
canvas = Canvas(root)


#  Making the corners of program rounded for operating systems that don't support it natively
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

# Create input labels and entry fields for all inputs
# Used .pack for ease
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

item_hired_label = tk.Label(root, text="Item Hired:")
item_hired_label.pack()
item_hired_entry = tk.Entry(root)
item_hired_entry.pack()

item_quantity_label = tk.Label(root, text="Item Quantity:")
item_quantity_label.pack()
item_quantity_entry = tk.Entry(root)
item_quantity_entry.pack()

receipt_number_label = tk.Label(root, text="Receipt Number:")
receipt_number_label.pack()
receipt_number_entry = tk.Entry(root)
receipt_number_entry.pack()


# Create a button to save the inputs and entry them into databse
enter_button = tk.Button(root, text="Enter", command=enter)
enter_button.pack()

# Create a display window for the databse on start
# Will be a empty window unless the show database button is pressed
record_viewer_window = tk.Toplevel(root)
record_viewer_window.title("Julie's Party Hire Record Keeper")

# Create a button to access the window displaying the inputs
record_viewer_button = tk.Button(root, text="Show Record Keeper", command=record_viewer)
record_viewer_button.pack()

# call the program to start it.
root.mainloop()
