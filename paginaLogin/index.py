
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro Widget")
        self.msg["font"] = ("Calibri", "9", "italic") # tive que colocar o Italic com letra minuscula rsrs-> resolução (italic)
        self.msg.pack () 
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack ()

    def mudarTexto(self, event):
        if self.msg["text"] == "Priemiro Widget":
            self.msg["text"] = "O Botão Receu um Clique"
        else:
            self.msg["text"] = "Primeiro Widget"

root = Tk()
Application(root)
root.mainloop()