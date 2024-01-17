import tkinter as tk
from tkinter import ttk
import db_product as db_product
from tkinter import messagebox as mb

class ProductsPage:
    
    def __init__(self, master):
        self.dbObject= db_product.Db()
        self.frame = tk.Frame(master, bg='white')
        
        label = tk.Label(self.frame, text="Página de Produtos")

        lblId= tk.Label(self.frame,text="ID do Produto")
        lblId.config(font=('varela round', 14),bg='#FF8100',fg="white")
       
        lblNome= tk.Label(self.frame,text= "Nome do Produto")
        lblNome.config(font=('varela round', 14),bg='#FF8100',fg="white")
       
        lblValor= tk.Label(self.frame,text= "Valor do Produto")
        lblValor.config(font=('varela round', 14),bg='#FF8100',fg="white")
       
        self.txtId = tk.Entry(self.frame, bd=3)
        self.txtNome = tk.Entry(self.frame)
        self.txtValor = tk.Entry(self.frame)

        btnCadastrar= tk.Button(self.frame,text='Cadastrar', height=150)
        btnAtualizar= tk.Button(self.frame,text='Atualizar')
        btnExcluir= tk.Button(self.frame,text='Excluir')
        btnLimpar= tk.Button(self.frame,text='Cadastrar')
       
        lblId.grid(row=1, column=0, sticky=tk.E,padx=10)
        lblNome.grid(row=1, column=1, sticky=tk.E)
        lblValor.grid(row=1, column=2, sticky=tk.E)

        self.txtId.grid(row=2, column=0)
        self.txtNome.grid(row=2, column=1)
        self.txtValor.grid(row=2, column=2)

        columns = ("ID", "Nome", "Valor")

        self.treeProducts = ttk.Treeview(self.frame, columns=columns, show="headings",selectmode='browse')
        self.verscrlbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.treeProducts.yview)
        self.verscrlbar.grid(row=5, column=8, sticky="ns")
        self.treeProducts.configure(yscrollcommand=self.verscrlbar.set)
        self.treeProducts.bind("<<TreeviewSelect>>", 
                               self.presentSelectedRecords)

        for col in columns:
            self.treeProducts.heading(col, text=col)
            self.treeProducts.column(col, width=100)  

        self.treeProducts.grid(row=5, column=0, columnspan=8, pady=10)
        

        btnCadastrar = tk.Button(self.frame, text='Cadastrar', command=self.fRegisterProduct)
        btnAtualizar = tk.Button(self.frame, text='Atualizar',command=self.fUpdateProduct)
        btnExcluir = tk.Button(self.frame, text='Excluir',command=self.fDeleteProduct)
        btnLimpar = tk.Button(self.frame, text='Limpar',command=self.fCleanScreen)

        btnCadastrar.grid(row=4, column=0, columnspan=2, pady=10)
        btnAtualizar.grid(row=4, column=2, columnspan=2, pady=10)
        btnExcluir.grid(row=4, column=4, columnspan=2, pady=10)
        btnLimpar.grid(row=4, column=6, columnspan=2, pady=10)

        self.loadInitialData()

    def errorInsert(self):
      mb.showerror("Erro", "Desculpe, não foi possível inserir o produto!")

    def successInsert(self):
      mb.showinfo("Sucesso", "O produto foi inserido com sucesso!")

    def errorUpdate(self):
      mb.showerror("Erro", "Desculpe, não foi possível atualizar o produto!")

    def successUpdate(self):
      mb.showinfo("Sucesso", "O produto foi atualizado com sucesso!")

    def verification():
      if mb.askyesno('Exclusão', 'Realmente quer excluir?'):
        mb.showwarning('Yes', 'Produto excluido com sucesso')
      

    def presentSelectedRecords(self, event):  
        self.fCleanScreen()  
        for selection in self.treeProducts.selection():  
            item = self.treeProducts.item(selection)  
            id_produto,nome,valor = item["values"][0:3]  
            self.txtId.insert(0, id_produto)  
            self.txtNome.insert(0, nome)  
            self.txtValor.insert(0, valor)

    def loadInitialData(self):
        try:
          self.id = 0
          self.iid = 0          
          registros=self.dbObject.selectData()
          print("************ dados disponíveis no BD ***********")        
          for item in registros:
              id_produto=item[0]
              nome=item[1]
              valor=item[2]
              print("ID = ", id_produto)
              print("Nome = ", nome)
              print("Valor  = ", valor, "\n")
                        
              self.treeProducts.insert('', 'end',
                                   iid=self.iid,                                   
                                   values=(id_produto,
                                           nome,
                                           valor))                        
              self.iid = self.iid + 1
              self.id = self.id + 1
        except:
          print('Ainda não existem dados para carregar')

    def fReadFields(self):
        try:
          print("************ dados dsponíveis ***********") 
          id_produto = int(self.txtId.get())
          print('id', id)
          nome=self.txtNome.get()
          print('nome', nome)
          valor=float(self.txtValor.get())          
          print('valor', valor)
          print('Read of the data with sucess!')        
        except:
          print('Não foi possível ler os dados.')
        return id_produto, nome, valor        
       
    def fRegisterProduct(self):
        try:
          print("************ dados dsponíveis ***********") 
          id_produto, nome, valor= self.fReadFields()                    
          self.dbObject.insertData(id_produto, nome, valor)                    
          self.treeProducts.insert('', 'end',
                                iid=self.iid,                                   
                                values=(id_produto,
                                        nome,
                                        valor))                        
          self.iid = self.iid + 1
          self.id = self.id + 1
          self.fCleanScreen()
          self.successInsert()        
        except:
         self.errorInsertInsert()  

    def fUpdateProduct(self):
        try:
          print("************ dados dsponíveis ***********")        
          id_produto, nome, valor= self.fReadFields()
          self.dbObject.updateData(id_produto, nome, valor)    
          self.treeProducts.delete(*self.treeProducts.get_children()) 
          self.loadInitialData()
          self.fCleanScreen()
          self.successUpdate()        
        except:
          self.errorUpdate()

    def fDeleteProduct(self):
        try:
          print("************ dados dsponíveis ***********")        
          id_produto, nome, valor= self.fReadFields()
          if mb.askyesno('Exclusão', 'Realmente quer excluir?'):
            mb.showinfo('Yes', 'Produto excluido com sucesso') 
            self.dbObject.deleteData(id_produto) 
            self.treeProducts.delete(*self.treeProducts.get_children()) 
            self.loadInitialData()
            self.fCleanScreen()
          else:
            mb.showinfo('No', 'A exclusão foi cancelada')
        except:
          print('Não foi possível fazer a exclusão do produto.')

    def fCleanScreen(self):
        try:
          print("************ dados dsponíveis ***********")        
          self.txtId.delete(0, tk.END)
          self.txtNome.delete(0, tk.END)
          self.txtValor.delete(0, tk.END)
          print('Campos Limpos!')        
        except:
          print('Não foi possível limpar os campos.')