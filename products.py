import os
import tkinter as tk
import dotenv
import pymysql
import requests
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw
import tkinter.font as tkFont
dotenv.load_dotenv()

class ProductsPage:
    
    def __init__(self, master):
        self.frame = tk.Frame(master, bg='white')
        
        label = tk.Label(self.frame, text="Página de Produtos")

        lblId= tk.Label(self.frame,text="ID do Produto")
        lblId.config(font=('varela round', 14),bg='#FF8100',fg="white")
       
        lblNome= tk.Label(self.frame,text= "Nome do Produto")
        lblNome.config(font=('varela round', 14),bg='#FF8100',fg="white")
       
        lblPreco= tk.Label(self.frame,text= "Preço do Produto")
        lblPreco.config(font=('varela round', 14),bg='#FF8100',fg="white")
       
        self.txtId = tk.Entry(self.frame, bd=3)
        self.txtNome = tk.Entry(self.frame)
        self.txtPreco = tk.Entry(self.frame)

        btnCadastrar= tk.Button(self.frame,text='Cadastrar', height=150)
        btnAtualizar= tk.Button(self.frame,text='Atualizar')
        btnExcluir= tk.Button(self.frame,text='Excluir')
        btnLimpar= tk.Button(self.frame,text='Cadastrar')
       
        lblId.grid(row=1, column=0, sticky=tk.E)
        lblNome.grid(row=1, column=1, sticky=tk.E)
        lblPreco.grid(row=1, column=2, sticky=tk.E)

        self.txtId.grid(row=2, column=0)
        self.txtNome.grid(row=2, column=1)
        self.txtPreco.grid(row=2, column=2)

        btnCadastrar = tk.Button(self.frame, text='Cadastrar')
        btnAtualizar = tk.Button(self.frame, text='Atualizar')
        btnExcluir = tk.Button(self.frame, text='Excluir')
        btnLimpar = tk.Button(self.frame, text='Limpar')

        btnCadastrar.grid(row=4, column=0, columnspan=2, pady=10)
        btnAtualizar.grid(row=4, column=2, columnspan=2, pady=10)
        btnExcluir.grid(row=4, column=4, columnspan=2, pady=10)
        btnLimpar.grid(row=4, column=6, columnspan=2, pady=10)

    def openConnection(self):
     try:
      self.connection= pymysql.connect(
        host= os.getenv("DB_HOST"),
        database=  os.getenv("DB_DATABASE"),
        user=  os.getenv("DB_USER"),
        password=  os.getenv("DB_PASSWORD"),
      )
      
     except (Exception, pymysql.Error) as error:
      if(self.connection):
        print ("Fail to connect to the Database",error)
      
        
    def selectData(self):
     try:
      self.openConnection()
      cursor= self.connection.cursor()
      selectQuery= "SELECT * FROM produtos"

      cursor.execute(selectQuery)
      registers= cursor.fetchall()
      
     except (Exception, pymysql.Error) as error:
      print ("Error in select operation",error)

     finally:
      
      if (self.connection):
        cursor.close()
        self.connection.close()
        print("The connection was closed")
        return registers

    def insertData(self,id,nome,valor):
     try:
        self.openConnection()
        cursor= self.connection.cursor()
        insertQuery= "INSERT INTO produtos (nome,valor) VALUES(%s, %s)", (value1,value2)
        recordInsert= (id,nome,valor)
        cursor.execute(insertQuery,recordInsert)
        self.connection.commit()
        count= cursor.rowcount()
        print (count, "Register inserted with success in the Products Table")

     except (Exception, pymysql.Error) as error:

      if(self.connection):
        print ("Fail to insert on the Products table",error)

     finally:
          
          if (self.connection):
            cursor.close()
            self.connection.close()
            print("The connection was closed")

    def updateData(self,id,nome,valor):
      try:
          self.openConnection()
          cursor= self.connection.cursor()
          print ("Register before the Upgrade")
          selectedQuery= """SELECT * FROM "produtos" where "id"= %s"""
          cursor.execute(selectedQuery,(id,))
          record= cursor.fetchone()

          sqlUpdate= """UPDATE produtos SET "nome" = %s,"valor"= %s  WHERE "id"= %s"""
          self.connection.commit()
          count = cursor.rowcount
          print (count, "Register updated with success!")
          print ("Register after the Upgrade")
          selectedQuery= """SELECT * FROM "produtos" where "id"= %s"""
          cursor.execute(sqlUpdate, (id,))
          record= cursor.fetchone()
          
      except (Exception, pymysql.Error) as error:
        print ("Fail on upgrade",error)

      finally:
          
          if (self.connection):
            cursor.close()
            self.connection.close()
            print("The connection was closed")

    def deleteData(self,id):
      try:
        self.openConnection()
        cursor= self.connection.cursor()
        deleteQuery= """DELETE from produtos WHERE "id"= %s"""
        cursor.execute(deleteQuery,(id,))

        self.connection.commit()
        count= cursor.rowcount()
        print (count, "Register deleted with success in the Products Table")

      except (Exception, pymysql.Error) as error:
        print ("Fail to delete on the Products table",error)

      finally:
          
          if (self.connection):
            cursor.close()
            self.connection.close()
            print("The connection was closed")
        
