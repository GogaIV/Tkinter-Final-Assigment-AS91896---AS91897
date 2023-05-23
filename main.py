import tkinter as tk
from tkinter import *
import base64, zlib
import tempfile
from tkinter import messagebox


#   Making a transparent window icon instead of a feather
ICON = zlib.decompress(
    base64.b64decode(
        "eJxjYGAEQgEBBiDJwZDBy"
        "sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc="
    )
)
_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, "wb") as icon_file:
    icon_file.write(ICON)


#  Creating the submit function that then is used to input
#  box entries which can also be updated with the same function
def submit():
    # Checks if item quantity inputted is a number
    try:
        item_quantity_input_interger = item_quantity_entry.get()
        int(item_quantity_input_interger)
    except ValueError:
        messagebox.showerror("Error", "Please enter number!")

    # Then checks if item quantity inputted is a number within 500 otherwise becomes invalid
    if item_quantity_input_interger > 500:
        messagebox.showerror("Error", "Please enter a number within 500!")
        item_quantity_entry = " "

    #  Get users input from input boxes
    name = name_entry.get()
    item_hired = item_hired_entry.get()
    item_quantity = item_quantity_entry.get()
    receipt_number = receipt_number_entry.get()

    #  Add records to the listbox. The submit function only works if listbox already exists
    information_list.append((name, item_hired, item_quantity, receipt_number))

    #  Updates the listboxs with a new entry if a new entry exists in the entry boxes. Both these
    # functions fit in the submit command. Even though they both do the same thing, they don't repeat twice
    # The below function creates display_text and then adds all the the input fields
    # to the into the listbox.
    display_text = (
        f"     {name}       \t{item_hired}\t{item_quantity}\t{receipt_number}"
    )
    # Makes a display for the listbox
    listbox.insert(tk.END, display_text)

    # Clear entry fields after the submit function is pressed
    name_entry.delete(0, tk.END)
    item_hired_entry.delete(0, tk.END)
    item_quantity_entry.delete(0, tk.END)
    receipt_number_entry.delete(0, tk.END)


# Making a function to open the window that shows the listbox
# and showing the inputs from the entry boxes.
def open_information_window():
    info_window = tk.Toplevel(root)
    info_window.title("Record Viewer")
    info_window.geometry("400x300")

    # Create a label for variable names on the second page
    label_text = "Name\tItem Hired\tItem Quantity\tReceipt Number"
    label = tk.Label(info_window, text=label_text)
    label.pack(padx=20, pady=6)

    #  Sets the width of the listbox when placing it on the page.
    label_width = max(len(label["text"]) for label in labels_widgets)
    listbox_width = label_width * 6  #  Adjust the factor to desired width

    #  Creating the listbox to display the record and making it global to be used outside function
    global listbox
    listbox = tk.Listbox(info_window, height=10, width=listbox_width)
    listbox.pack(padx=20, pady=10)

    #  Insert initial variable values into the listbox. THIS CODE WILL NOT UPDATE THE LISTBOX
    for info in information_list:
        display_text = f"{info[0]}\t{info[1]}\t{info[2]}\t{info[3]}"
        listbox.insert(tk.END, display_text)

    # Makes function to delete listbox vairables when clicked on then clicked the button
    def delete_selected():
        selected_index = listbox.curselection()
        if selected_index:
            listbox.delete(selected_index)

    #  Create delete button for second page
    delete_button = tk.Button(info_window, text="Delete", command=delete_selected)
    delete_button.pack(pady=10)


#  Creates the program window and chooses the window icon to be transparent
root = tk.Tk()
root.iconbitmap(default=ICON_PATH)
root.title("Receipt Manager")
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


# Create labels and entry fields. First are all the labels
# This is the most efficient way to to creat all of them. This puts them into a list
labels = ["Name:", "Item Hired:", "Item Quantity:", "Receipt Number:"]
labels_widgets = []  #  Keep track of label widgets that are created
entries = []  # Keeps track of the entires created.
# After all labels were placed in a list the followinf code chooses one and then places
#  it on the grid in a seperate line each time
for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, sticky=tk.W)
    labels_widgets.append(
        label
    )  #  Add label widget to the list so that it can be seen on the program
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entries.append(entry)


name_entry = entries[0]
item_hired_entry = entries[1]
item_quantity_entry = entries[2]
receipt_number_entry = entries[3]

#  Create submit button for all the
submit_button = tk.Button(
    root,
    text="Submit",
    command=submit,
)
submit_button.grid(row=len(labels), column=0, columnspan=2)

#  Create open record window button
open_info_button = tk.Button(
    root, text="Open Record Viewing Page", command=open_information_window
)
open_info_button.grid(row=len(labels) + 1, column=0, columnspan=2)

#  Create list to store the record
information_list = []

root.mainloop()
