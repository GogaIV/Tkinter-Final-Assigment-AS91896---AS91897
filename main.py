from tkinter import *

#Creating window for program
root=Tk()
root.minsize(height=300, width=400)
root.title("Party Hire Store Record Keeper")

#Creating the main menu
def Menu():

        #Making record keeper page
    def recordpage():
        root.minsize()
        #Add a message box for errors


    #Making Record Viewing page
    def viewrecordspage():
        root.minsize()
        menubutton_1.destroy()
        menubutton_2.destroy()

    
    #Labeling the main menu
    label_1 = Label(root, text="Main Menu")
    label_1.grid(column=2, row=1)

    #Making buttons to seperate 
    menubutton_1 = Button(root, text="Add a Record", command=recordpage, activebackground="white")
    menubutton_1.grid(column=1, row=2)
    menubutton_2 = Button(root, text="View Records", command=viewrecordspage, activebackground="white")
    menubutton_2.grid(column=2, row=2)




Menu()
root.mainloop()