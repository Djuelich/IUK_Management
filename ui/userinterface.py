from Tkinter import *

from PIL import Image, ImageTk


mainUi = Tk()
mainUi.title("IUK_Management")

screen_width = mainUi.winfo_screenwidth()/4
screen_height = mainUi.winfo_screenheight()/2

mainUi.geometry('{}x{}'.format(screen_width, screen_height))

class MainUi(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open("/home/joker/Schreibtisch/IUK_Management/res/elw.png")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        self.label = Label(master, text="login")
        

        

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)



e = MainUi(mainUi)
e.pack(fill=BOTH, expand=YES)
label = MainUi(mainUi)
label.pack(pady=100, side=TOP)


mainUi.mainloop()