import pymysql
import pandas as pd

class DatabaseHandler:
    def __init__(self, host, user, password, database):
        self.conn = pymysql.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, values):
        self.cursor.execute(query, values)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

def insert_data_to_database(db_handler, df):
    for index, row in df.iterrows():
        query = "INSERT INTO productos (Producto, Comentarios, Precio, Tipo_de_envio, Descuento, Precio_anterior) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (row['Producto'], row['Comentarios'], row['Precio'], row['Tipo_de_envio'], row['Descuento'], row['Precio_anterior'])
        db_handler.execute_query(query, values)

def main():
    db_handler = DatabaseHandler(host='localhost', user='root', password='030509rr', database='proyecto1')
    df = pd.read_csv('Datasets/Limpios_ClaroShop.csv')

    insert_data_to_database(db_handler, df)

    db_handler.close_connection()
    print("Datos insertados correctamente.")

if __name__ == "__main__":
    main()

