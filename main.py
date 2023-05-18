from tkinter import *
from tkcalendar import *

#Creating window for program
root=Tk()
root.minsize(height=200, width=170)
root.title("Party Hire Store Record Keeper")
canvas = Canvas(root)


#Making the program look better with rounded corners
def round_rectangle_border(x1, y1, x2, y2, radius=25, **kwargs):
        
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius, 
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

my_rectangle = round_rectangle_border(50, 50, 150, 100, radius=20, fill="blue")


#Creating the main menu
def Menu():

        #Making record keeper page
    def recordpage():
        root.minsize(height=200, width=170)


        #Making everything global to be used on the back function
        global customernamelabel
        global itemhiredlabel
        global itemquantitylabel
        global recipetnumlabel


        #Labels for the input boxes
        customernamelabel = Label(root,text="Customer Name")
        customernamelabel.grid(column=1,row=2)
        itemhiredlabel = Label(root,text="Hired Item")
        itemhiredlabel.grid(column=2,row=2)
        itemquantitylabel = Label(root,text="Item Quantity")
        itemquantitylabel.grid(column=3,row=2)
        recipetnumlabel = Label(root,text="Recipet Number")
        recipetnumlabel.grid(column=4,row=2)

        #Input boxes

        #Destorying previous page elemnts
        menubutton_1.destroy()
        menubutton_2.destroy()
        menubutton_3.destroy()
        label_1.destroy()
        emptylabel1.destroy()
        emptylabel2.destroy()

        #Adding back button for record keeping page
        global button_2
        button_2= Button(root,text="<--Menu", width="7", command=back, activebackground="red")
        button_2.grid(column=1,row=1, sticky=W)

        #Add a message box for errors


    #Making Record Viewing page
    def viewrecordspage():
        root.minsize(height=200, width=170)
        label_1.destroy()
        menubutton_1.destroy()
        menubutton_2.destroy()
        menubutton_3.destroy()
        emptylabel1.destroy()
        emptylabel2.destroy()

        #Making everything global to be used on the back function
        global customernamelabel
        global itemhiredlabel
        global itemquantitylabel
        global recipetnumlabel


        #Labels for the grid boxes
        customernamelabel = Label(root,text="Customer Name")
        customernamelabel.grid(column=1,row=2)
        itemhiredlabel = Label(root,text="Hired Item")
        itemhiredlabel.grid(column=2,row=2)
        itemquantitylabel = Label(root,text="Item Quantity")
        itemquantitylabel.grid(column=3,row=2)
        recipetnumlabel = Label(root,text="Recipet Number")
        recipetnumlabel.grid(column=4,row=2)

        
        #Adding back button for record viewing page
        global button_2
        button_2= Button(root,text="<--Menu", width="7", command=back, activebackground="red")
        button_2.grid(column=1,row=1,sticky=W)
        

    def helppage():
        root.minsize(height=200, width=170)
        label_1.destroy()
        menubutton_1.destroy()
        menubutton_2.destroy()
        menubutton_3.destroy()
        emptylabel1.destroy()
        emptylabel2.destroy()

        #Adding back button for help page
        global button_2
        button_2= Button(root,text="<--Menu", width="7", command=back, activebackground="red")
        button_2.grid(column=1,row=1)




        #Making a back button that can be used on all pages. 
    def back():
        root.minsize(height=200, width=170)
        root.title("Party Hire Store Record Keeper")
        Menu()
        #removing the back button
        button_2.destroy()
        #Removing the other assests,  buttons and labels
        customernamelabel.destroy()
        itemhiredlabel.destroy()
        itemquantitylabel.destroy()
        recipetnumlabel.destroy()
        


    #Labeling the main menu
    label_1 = Label(root, text="Main Menu")
    label_1.grid(column=2, row=1)

    #Making buttons to seperate 
    menubutton_1 = Button(root, text="Add a Record", command=recordpage, activebackground="white")
    menubutton_1.grid(column=2, row=2)
    menubutton_2 = Button(root, text="View Records", command=viewrecordspage, activebackground="white")
    menubutton_2.grid(column=2, row=3)
    menubutton_3 = Button(root, text="How to Use?", command=helppage, activebackground="white")
    menubutton_3.grid(column=2, row=4)

    #Adding a spacing between sides and menu
    emptylabel1 = Label(root, text="", padx= 20)
    emptylabel1.grid(column=1,row=2)
    emptylabel2 = Label(root, text="", padx= 20)
    emptylabel2.grid(column=3,row=2)





Menu()
root.mainloop()