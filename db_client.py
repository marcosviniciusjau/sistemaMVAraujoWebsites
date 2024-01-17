  
import os

import pymysql


class Db:
   
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
      selectQuery= "SELECT * FROM clientes"

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

  def insertData(self,id_cliente,nome,valor):
     try:
        self.openConnection()
        cursor= self.connection.cursor()
        insertQuery= "INSERT INTO clientes (id_cliente,nome,valor) VALUES(%s,%s, %s)"
        recordInsert= (id_cliente,nome,valor)
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

  def updateData(self, id_cliente, nome, valor):
    try:
        self.openConnection()
        cursor = self.connection.cursor()
        
        print("Register before the Upgrade")
        selectedQuery = """SELECT * FROM clientes WHERE id_cliente = %s"""
        cursor.execute(selectedQuery, (id_cliente,))
        record_before = cursor.fetchone()

        sqlUpdate = """UPDATE clientes SET nome = %s, valor = %s WHERE id_cliente = %s"""
        cursor.execute(sqlUpdate, (nome, valor, id_cliente))
        self.connection.commit()
        count = cursor.rowcount
        print(count, "Register updated with success!")

        print("Register after the Upgrade")
        cursor.execute(selectedQuery, (id_cliente,))
        record_after = cursor.fetchone()
        print("Before:", record_before)
        print("After:", record_after)

    except (Exception, pymysql.Error) as error:
        print("Fail on upgrade", error)

    finally:
        if self.connection:
            cursor.close()
            self.connection.close()
            print("The connection was closed")


  def deleteData(self, id_cliente):
    try:
        self.openConnection()
        cursor = self.connection.cursor()

        deleteQuery = """DELETE from clientes WHERE id_cliente = %s"""
        cursor.execute(deleteQuery, (id_cliente,))
        self.connection.commit()
        count = cursor.rowcount()
        print(count, "Register deleted with success in the Products Table")

        print("Check if the register was deleted:")
        selectedQuery = """SELECT * FROM clientes WHERE id_cliente = %s"""
        cursor.execute(selectedQuery, (id_cliente,))
        record_after_deletion = cursor.fetchone()
        if record_after_deletion is None:
            print("Register was successfully deleted.")
        else:
            print("Failed to delete the register.")

    except (Exception, pymysql.Error) as error:
        print("Fail to delete on the Products table", error)

    finally:
        if self.connection:
            cursor.close()
            self.connection.close()
            print("The connection was closed")

        