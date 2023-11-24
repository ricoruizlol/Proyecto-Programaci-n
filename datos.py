import csv
import mysql.connector

# Establece la conexión a MySQL
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="12345678",
    database="proyecto5"
)

# Crea un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Abre el archivo CSV y realiza la inserción de datos
with open('Datasets/Limpios_ClaroShop.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)

    # Ignora la primera fila si contiene encabezados
    next(lector_csv)

    # Define el comando SQL para la inserción
    insertar_datos = """
    INSERT INTO productos (Producto, Comentarios, Precio, Tipo_de_envio, Descuento, Precio_anterior)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Itera sobre las filas del archivo CSV e inserta los datos en la base de datos
    for fila in lector_csv:
        cursor.execute(insertar_datos, tuple(fila))

# Cierra el cursor y aplica los cambios en la base de datos
cursor.close()
conexion.commit()

# Cierra la conexión
conexion.close()

print("Datos insertados exitosamente desde el archivo CSV.")