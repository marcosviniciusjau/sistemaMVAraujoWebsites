import tkinter as tk
from PIL import Image, ImageTk

class HomePage:
    
    def __init__(self, master):
        self.frame = tk.Frame(master, bg='white')
        self.image = Image.open("logo.PNG")
        self.image_tk = ImageTk.PhotoImage(self.image)

        self.canvas = tk.Canvas(self.frame, width=400, height=1020)
        self.menubutton = tk.Menubutton(self.frame, image=self.image_tk)
        self.menubutton.image = None
        self.menubutton.image = self.image_tk
        self.menubutton.grid(row=0, column=1, sticky='nsew')