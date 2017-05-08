from Tkinter import *
from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH, RAISED, RIGHT
from ttk import Frame, Style, Button
from tkFileDialog import askopenfilename


class Example(Frame):


    def abrir(self):
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

        bard = Image.open(filename)
        bard = bard.resize((400,550), Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=10, y=25)


    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()



    def initUI(self):
        self.parent.title("Tomates")
        self.pack(fill=BOTH, expand=1)
        Style().configure("TFrame", background="#333")

        AbrirButton = Button(self, text="Abrir")
        AbrirButton.pack(side=RIGHT, padx=5, pady=5)
        AbrirButton.place(x=800, y=25)
        AbrirButton["command"] = self.abrir

        #var = StringVar()
        #label1 = Label( self, textvariable=var)
        #label1.place(x=20, y=30)


        #var.set("Hey!? How are you doing?")
        #label1.pack()
        label = Label(self, text="Analisis")
        label.place(x=600, y=25)

        label = Label(self, text="Salida1:")
        label.place(x=500, y=150)

        label = Label(self, text="Salida2:")
        label.place(x=500, y=200)

        label = Label(self, text="Salida3:")
        label.place(x=500, y=250)

        label = Label(self, text="Estado del Tomate: ")
        label.place(x=500, y=300)


        label = Label(self, text="0.012")
        label.place(x=700, y=150)

        label = Label(self, text="0.120302")
        label.place(x=700, y=200)

        label = Label(self, text="0.9")
        label.place(x=700, y=250)

        label = Label(self, text="Maduro")
        label.place(x=700, y=300)


def main():
    root = Tk()
    root.geometry("900x600")
    root.resizable(False,False)
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
