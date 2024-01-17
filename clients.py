import tkinter as tk
from tkinter import ttk
import db_client as db_client
from tkinter import messagebox as mb

class ClientsPage:
    
    def __init__(self, master):
        self.dbObject= db_client.Db()
        self.frame = tk.Frame(master, bg='white')
        
        lblId= tk.Label(self.frame,text="ID do Cliente")
        lblId.config(font=('varela round', 14),bg='#FF8100',fg="white")
       
        lblNome= tk.Label(self.frame,text= "Nome do Cliente")
        lblNome.config(font=('varela round', 14),bg='#FF8100',fg="white")
       
        lblData= tk.Label(self.frame,text= "Data de Nascimento")
        lblData.config(font=('varela round', 14),bg='#FF8100',fg="white")

        lblCep= tk.Label(self.frame,text= "CEP")
        lblCep.config(font=('varela round', 14),bg='#FF8100',fg="white")

        lblEndereco= tk.Label(self.frame,text= "Endereço")
        lblEndereco.config(font=('varela round', 14),bg='#FF8100',fg="white")
       
        lblCidade= tk.Label(self.frame,text= "Cidade")
        lblCidade.config(font=('varela round', 14),bg='#FF8100',fg="white")
       
       
        self.txtId = tk.Entry(self.frame, bd=3)
        self.txtNome = tk.Entry(self.frame)
        self.txtData = tk.Entry(self.frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.txtCep = tk.Entry(self.frame)
        self.txtEndereco = tk.Entry(self.frame)
        self.txtCidade= tk.Entry(self.frame) 

        btnCadastrar= tk.Button(self.frame,text='Cadastrar', height=150)
        btnAtualizar= tk.Button(self.frame,text='Atualizar')
        btnExcluir= tk.Button(self.frame,text='Excluir')
        btnLimpar= tk.Button(self.frame,text='Cadastrar')
       
        lblId.grid(row=1, column=0, sticky=tk.E, padx=10)
        lblNome.grid(row=1, column=1, sticky=tk.E)
        lblData.grid(row=2, column=0, sticky=tk.E)
        lblCep.grid(row=2, column=1, sticky=tk.E, padx=10)
        lblEndereco.grid(row=3, column=0, sticky=tk.E)
        lblCidade.grid(row=3, column=1, sticky=tk.E, padx=10)

        self.txtId.grid(row=2, column=0)
        self.txtNome.grid(row=2, column=1)
        self.txtData.grid(row=3, column=0)
        self.txtCep.grid(row=3, column=1)
        self.txtEndereco.grid(row=4, column=0)
        self.txtCidade.grid(row=4, column=1)

        columns = ("ID", "Nome", "Data Nascimento", "CEP", "Endereço", "Cidade")

        self.treeClients = ttk.Treeview(self.frame, columns=columns, show="headings",selectmode='browse')
        self.verscrlbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.treeClients.yview)
        self.verscrlbar.grid(row=5, column=8, sticky="ns")
        self.treeClients.configure(yscrollcommand=self.verscrlbar.set)
        self.treeClients.bind("<<TreeviewSelect>>", 
                               self.presentSelectedRecords)

        for col in columns:
            self.treeClients.heading(col, text=col)
            self.treeClients.column(col, width=100)  

        self.treeClients.grid(row=5, column=0, columnspan=8, pady=10)
        

        btnCadastrar = tk.Button(self.frame, text='Cadastrar', command=self.fRegisterClient)
        btnAtualizar = tk.Button(self.frame, text='Atualizar',command=self.fUpdateClient)
        btnExcluir = tk.Button(self.frame, text='Excluir',command=self.fDeleteClient)
        btnLimpar = tk.Button(self.frame, text='Limpar',command=self.fCleanScreen)

        btnCadastrar.grid(row=4, column=0, columnspan=2, pady=10)
        btnAtualizar.grid(row=4, column=2, columnspan=2, pady=10)
        btnExcluir.grid(row=4, column=4, columnspan=2, pady=10)
        btnLimpar.grid(row=4, column=6, columnspan=2, pady=10)

        self.loadInitialData()

    def errorInsert(self):
      mb.showerror("Erro", "Desculpe, não foi possível inserir o cliente!")

    def successInsert(self):
      mb.showinfo("Sucesso", "O cliente foi inserido com sucesso!")

    def errorUpdate(self):
      mb.showerror("Erro", "Desculpe, não foi possível atualizar o cliente!")

    def successUpdate(self):
      mb.showinfo("Sucesso", "O cliente foi atualizado com sucesso!")

    def verification():
      if mb.askyesno('Exclusão', 'Realmente quer excluir?'):
        mb.showwarning('Yes', 'Cliente excluido com sucesso')
      

    def presentSelectedRecords(self, event):  
        self.fCleanScreen()  
        for selection in self.treeclients.selection():  
            item = self.treeclients.item(selection)  
            id_cliente,nome,valor = item["values"][0:3]  
            self.txtId.insert(0, id_cliente)  
            self.txtNome.insert(0, nome)  
            self.txtValor.insert(0, valor)

    def loadInitialData(self):
        try:
          self.id = 0
          self.iid = 0          
          registros=self.dbObject.selectData()
          print("************ dados disponíveis no BD ***********")        
          for item in registros:
              id_cliente=item[0]
              nome=item[1]
              valor=item[2]
              print("ID = ", id_cliente)
              print("Nome = ", nome)
              print("Valor  = ", valor, "\n")
                        
              self.treeClients.insert('', 'end',
                                   iid=self.iid,                                   
                                   values=(id_cliente,
                                           nome,
                                           valor))                        
              self.iid = self.iid + 1
              self.id = self.id + 1
        except:
          print('Ainda não existem dados para carregar')

    def fReadFields(self):
        try:
          print("************ dados dsponíveis ***********") 
          id_cliente = int(self.txtId.get())
          print('id', id)
          nome=self.txtNome.get()
          print('nome', nome)
          valor=float(self.txtValor.get())          
          print('valor', valor)
          print('Read of the data with sucess!')        
        except:
          print('Não foi possível ler os dados.')
        return id_cliente, nome, valor        
       
    def fRegisterClient(self):
        try:
          print("************ dados dsponíveis ***********") 
          id_cliente, nome, valor= self.fReadFields()                    
          self.dbObject.insertData(id_cliente, nome, valor)                    
          self.treeClients.insert('', 'end',
                                iid=self.iid,                                   
                                values=(id_cliente,
                                        nome,
                                        valor))                        
          self.iid = self.iid + 1
          self.id = self.id + 1
          self.fCleanScreen()
          self.successInsert()        
        except:
         self.errorInsertInsert()  

    def fUpdateClient(self):
        try:
          print("************ dados dsponíveis ***********")        
          id_cliente, nome, valor= self.fReadFields()
          self.dbObject.updateData(id_cliente, nome, valor)    
          self.treeClients.delete(*self.treeClients.get_children()) 
          self.loadInitialData()
          self.fCleanScreen()
          self.successUpdate()        
        except:
          self.errorUpdate()

    def fDeleteClient(self):
        try:
          print("************ dados dsponíveis ***********")        
          id_cliente, nome, valor= self.fReadFields()
          if mb.askyesno('Exclusão', 'Realmente quer excluir?'):
            mb.showinfo('Yes', 'cliente excluido com sucesso') 
            self.dbObject.deleteData(id_cliente) 
            self.treeClients.delete(*self.treeClients.get_children()) 
            self.loadInitialData()
            self.fCleanScreen()
          else:
            mb.showinfo('No', 'A exclusão foi cancelada')
        except:
          print('Não foi possível fazer a exclusão do cliente.')

    def fCleanScreen(self):
        try:
          print("************ dados dsponíveis ***********")        
          self.txtId.delete(0, tk.END)
          self.txtNome.delete(0, tk.END)
          self.txtValor.delete(0, tk.END)
          print('Campos Limpos!')        
        except:
          print('Não foi possível limpar os campos.')