# Used to test code before entered into final  piece of code. Used so I don't need to
# Change all my code to test one function
import sqlite3
from tkinter import *


root = Tk()
root.minsize(height=200, width=170)
root.title("Party Hire Store Record Keeper")

conn = sqlite3.connect("pythonDB.db")
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS RecordONE (Number REAL, Name TEXT)")


def data_entry():
    number = 1234
    name = "GeeksforGeeks"
    c.execute("INSERT INTO RecordONE (Number, Name) VALUES(?, ?)", (number, name))
    conn.commit()


create_table()
data_entry()

c.close()
conn.close()

root.mainloop()
