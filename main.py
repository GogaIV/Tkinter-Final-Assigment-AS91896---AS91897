from tkinter import *

#Creating window for program
root=Tk()
root.minsize(height=150, width=150)
root.title("Party Hire Store Record Keeper")

#Creating the main menu
def Menu():
    #Labeling the main menu
    label_1 = Label(root, text="Main Menu")