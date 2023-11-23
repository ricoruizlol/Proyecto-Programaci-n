import mysql.connector

# Establece la conexión a MySQL
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="030509RR",
)

# Crea un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crea la base de datos
proyecto = "proyecto5"
cursor.execute(f"CREATE DATABASE {proyecto}")

# Cierra el cursor y la conexión
cursor.close()
conexion.close()

print(f"Base de datos '{proyecto}' creada exitosamente.")