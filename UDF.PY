import sqlite3
import pandas as pd

#creamos una funcion square para utilizarla en la bas de datos
square = lambda n : n*n

with sqlite3.connect("Northwind.db") as conn:
    conn.create_function("square",1,square)
    cursor = conn.cursor()
    cursor.execute('SELECT *,square(Price) FROM Products WHERE Price > 0')
    results = cursor.fetchall()
    results_df = pd.DataFrame(results)
print(results_df)

# print(square(10))

# #lee la bas de base de datos
# conn = sqlite3.connect("Northwind.db")
# conn.create_function("square", 1, square) 

# cursor = conn.cursor()
# #ejecuta la consulta en la base de datos
# cursor.execute('''
#     SELECT * FROM Products
#     ''')

# results = cursor.fetchall()
# #convierto en dataframe los resultados
# results_df = pd.DataFrame(results)

# #guardo los datos en la base de datos
# conn.commit()

# #cierra la conexion de cursor y de conn
# cursor.close()
# conn.close()

# #muestro los resultados en un dataframe
# print(results_df)