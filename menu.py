import tkinter as tk
from PIL import Image, ImageTk

from products import ProductsPage

from clients import ClientsPage

from requests import RequestsPage

from home import HomePage

class Menu:
    def __init__(self):
        
        self.janela = tk.Tk()
        self.janela.title("MV Araújo Websites Sistema") 
        self.janela.geometry('1320x1020')

        self.menu_frame = tk.Frame(self.janela, width=400, height=400, bg='#FF8100')
        self.menu_frame.grid(row=0, column=0, sticky='ns')

        self.home_btn = tk.Label(self.menu_frame, text='Home', cursor='hand2')
        self.home_btn.config(font=('varela round', 14),bg='#FF8100',fg="white")
        self.home_btn.pack(pady=10)
        self.home_btn.bind("<Button-1>", lambda event, page=HomePage: self.openPage(page))

        self.products_btn = tk.Label(self.menu_frame, text='Produtos', cursor='hand2')
        self.products_btn.config(font=('varela round', 14),bg='#FF8100',fg="white")
        self.products_btn.pack(pady=10)
        self.products_btn.bind("<Button-1>", lambda event, page=ProductsPage: self.openPage(page))

        self.clients_btn = tk.Label(self.menu_frame, text='Clientes', cursor='hand2')
        self.clients_btn.config(font=('varela round', 14),bg='#FF8100',fg="white",)
        self.clients_btn.pack(pady=10)
        self.clients_btn.bind("<Button-1>", lambda event, page=ClientsPage: self.openPage(page))
      
        self.requests_btn = tk.Label(self.menu_frame, text='Pedidos', cursor='hand2')
        self.requests_btn.config(font=('varela round', 14),bg='#FF8100',fg="white")
        self.requests_btn.pack(pady=10)
        self.requests_btn.bind("<Button-1>", lambda event, page=RequestsPage: self.openPage(page))
      
        
        self.image = Image.open("logo.PNG")
        self.image_tk = ImageTk.PhotoImage(self.image)

        self.canvas = tk.Canvas(self.janela, width=400, height=1020)
        self.menubutton = tk.Menubutton(self.janela, image=self.image_tk)
        self.menubutton.image = None
        self.menubutton.image = self.image_tk
        self.menubutton.grid(row=0, column=1, sticky='nsew')

        self.frames = {}

        self.janela.grid_rowconfigure(0, weight=1)
        self.janela.grid_columnconfigure(1, weight=1)

        self.janela.mainloop()


    def openPage(self, page_class):
        page_name = page_class.__name__
        if page_name not in self.frames:
            self.frames[page_name] = page_class(self.janela).frame

        for frame in self.frames.values():
            if frame == self.frames[page_name]:
                frame.grid(row=0, column=1, sticky='nsew')
            else:
                frame.grid_forget()

menu = Menu()
