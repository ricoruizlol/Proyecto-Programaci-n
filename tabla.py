import mysql.connector

# Establece la conexión a MySQL
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="030509RR",
    database="proyecto"
)

# Crea un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Define el comando SQL para crear la tabla
crear_tabla = """
CREATE TABLE productos (
  Producto VARCHAR(1024),
  Comentarios BIGINT,
  Precio DECIMAL(10, 2), 
  Tipo_de_envio VARCHAR(1024),
  Descuento DECIMAL(5, 2),
  Precio_anterior DECIMAL(10, 2) 
)
"""

# Ejecuta el comando SQL para crear la tabla
cursor.execute(crear_tabla)

# Cierra el cursor y aplica los cambios en la base de datos
cursor.close()
conexion.commit()

# Cierra la conexión
conexion.close()

print("Tabla 'productos' creada exitosamente.")