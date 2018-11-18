from Tkinter import * 



mainUi = Tk()

#If you have a large number of widgets, like it looks like you will for your
#game you can specify the attributes for all widgets simply like this.

screen_width = mainUi.winfo_screenwidth()/4
screen_height = mainUi.winfo_screenheight()/2
mainUi.title('IUK Management')
#You can set the geometry attribute to change the root windows size
mainUi.geometry('{}x{}'.format(screen_width, screen_height))
mainUi.resizable(0, 0) #Don't allow resizing in the x or y direction
mainUiLabel = Label(text = "IUK Management")

photo = PhotoImage(file = "/home/joker/Schreibtisch/IUK_Management/res/elw.png")
mainFrame = Frame(mainUi)
Label(mainUi, image=photo, height=screen_height, width=screen_width).place(x=0,y=0)


login = Label(mainUi, text = "Login")
login.place(x= 100, y = 100)
login.pack(pady=10, side=TOP)
login = Entry(mainUi)
login.pack(pady=20, side=TOP)



mainUi.mainloop()