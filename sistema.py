import pymysql
import os
import dotenv

dotenv.load_dotenv()

conn= pymysql.connect(
  host= os.getenv("DB_HOST"),
  database=  os.getenv("DB_DATABASE"),
  user=  os.getenv("DB_USER"),
  password=  os.getenv("DB_PASSWORD"),
)

cursor= conn.cursor()
cursor.execute("SELECT * FROM produtos")

registros= cursor.fetchall()

cursor.execute("INSERT INTO produtos (nome,valor) VALUES(%s, %s)", (valor1,valor2))
conn.commit()
cursor.execute("UPDATE produtos SET nome = %s WHERE valor=%s," (novo_valor,valor_de_referencia))
cursor.execute("DELETE FROM produtos WHERE nome = %s",  (valor_de_referencia))
conn.commit()
cursor.close()
conn.close()

for registro in registros:
  print (registro)
