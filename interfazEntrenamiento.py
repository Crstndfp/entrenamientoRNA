from Tkinter import *
from Tkinter import Tk
import Tkinter
from tkFileDialog import askopenfilename
from PIL import ImageTk
from PIL import Image


class Application(Frame):
    def say_hi(self):
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
        imagenAnchuraMaxima=600
        imagenAlturaMaxima=400
        img = Image.open(filename)
        img.thumbnail((imagenAnchuraMaxima,imagenAlturaMaxima), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(img)

        label=Tkinter.Label(root, image=tkimage, width=imagenAnchuraMaxima, height=imagenAlturaMaxima).pack()
        root.mainloop()


    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Abrir",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

        

        Label(text="one").pack()

        separator = Frame(height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        Label(text="two").pack()

        mainloop()


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.minsize(width=900,height=450)
        self.pack()
        self.createWidgets()




root = Tk()
root.title("Mostrar imagen")
root.resizable(width=400, height=600)
app = Application(master=root)
app.mainloop()
root.destroy()
