import os
import tkinter as tk
import dotenv
import pymysql
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw
import tkinter.font as tkFont
dotenv.load_dotenv()

class RequestsPage:
    
    def __init__(self, master):
        self.frame = tk.Frame(master, bg='white')
        label = tk.Label(self.frame, text="Página de Pedidos")
        label.pack(pady=20)
    
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
      selectQuery= "SELECT * FROM pedidos"

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

    def insertData(self,id,cliente_id,formpagamento,valor):
     try:
        self.openConnection()
        cursor= self.connection.cursor()
        insertQuery= "INSERT INTO pedidos (nome,valor) VALUES(%s, %s)", (value1,value2)
        recordInsert= (id,nome,valor)
        cursor.execute(insertQuery,recordInsert)
        self.connection.commit()
        count= cursor.rowcount()
        print (count, "Register inserted with success in the Requests Table")

     except (Exception, pymysql.Error) as error:

      if(self.connection):
        print ("Fail to insert on the Requests table",error)

     finally:
          
          if (self.connection):
            cursor.close()
            self.connection.close()
            print("The connection was closed")

    def updateData(self,id,cliente_id,formpagamento,valor):
      try:
          self.openConnection()
          cursor= self.connection.cursor()
          print ("Register before the Upgrade")
          selectedQuery= """SELECT * FROM "pedidos" where "id"= %s"""
          cursor.execute(selectedQuery,(id,))
          record= cursor.fetchone()

          sqlUpdate= """UPDATE pedidos SET "cliente_id" = %s,"formpagamento"= %s,"valor"= %s  WHERE "id"= %s"""
          self.connection.commit()
          count = cursor.rowcount
          print (count, "Register updated with success!")
          print ("Register after the Upgrade")
          selectedQuery= """SELECT * FROM "pedidos" where "id"= %s"""
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
        deleteQuery= """DELETE from pedidos WHERE "id"= %s"""
        cursor.execute(deleteQuery,(id,))

        self.connection.commit()
        count= cursor.rowcount()
        print (count, "Register deleted with success in the Requests Table")

      except (Exception, pymysql.Error) as error:
        print ("Fail to delete on the Requests table",error)

      finally:
          
          if (self.connection):
            cursor.close()
            self.connection.close()
            print("The connection was closed")
        
