-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS proyecto1;
USE proyecto1;

-- Crear la tabla productos
CREATE TABLE IF NOT EXISTS productos (
  Producto VARCHAR(1024),
  Comentarios BIGINT,
  Precio DECIMAL(10, 2),
  Tipo_de_envio VARCHAR(1024),
  Descuento DECIMAL(5, 2),
  Precio_anterior DECIMAL(10, 2)
);

-- Mostrar un mensaje indicando que la operación ha sido exitosa
SELECT 'Base de datos y tabla creadas correctamente' AS Mensaje;

SELECT * FROM productos;