import pandas as pd
import re

class LimpiadorCSV:
    def __init__(self, archivo):
        self.df = pd.read_csv(archivo)

    def eliminar_filas_vacias(self):
        columnas_a_considerar = self.df.columns.difference(['Comentarios'])
        self.df = self.df.dropna(subset=columnas_a_considerar)

    def limpiar_precio(self):
        def _limpiar_precio(valor):
            if isinstance(valor, str):
                valor = valor.replace('MXN', '').strip()
                partes = valor.split()
                if len(partes) > 1:
                    valor = partes[0]
                valor = valor.replace('$', '').replace(',', '').strip()
                return float(valor)
            return valor
        self.df['Precio'] = self.df['Precio'].apply(_limpiar_precio)

    def limpiar_descuento(self):
        self.df['Descuento'] = self.df['Descuento'].astype(str).str.replace('-', '').str.replace('%', '').astype(float)

    def rellenar_comentarios_vacios(self):
        self.df['Comentarios'] = self.df['Comentarios'].fillna(0)

    def eliminar_parentesis_comentarios(self):
        def _eliminar_parentesis_y_convertir(texto):
            if isinstance(texto, str):
                numero = re.sub(r'[()]', '', texto)
                return int(numero)
            return texto
        self.df['Comentarios'] = self.df['Comentarios'].apply(_eliminar_parentesis_y_convertir)

    def quitar_signo_dolar(self):
        self.df['Precio anterior'] = self.df['Precio anterior'].astype(str).str.replace('$', '')

    def limpiar_precio_anterior(self):
        def _limpiar_precio_anterior(valor):
            if isinstance(valor, str):
                valor = valor.replace(',', '').strip()
                return float(valor)
            return valor
        self.df['Precio anterior'] = self.df['Precio anterior'].apply(_limpiar_precio_anterior)

    def ordenar_por_producto(self):
        self.df = self.df.sort_values(by='Producto')

    def eliminar_duplicados(self):
        self.df = self.df.drop_duplicates()

    def guardar_csv(self, archivo_salida):
        self.df.to_csv(archivo_salida, index=False)

# Uso de la clase
limpiador = LimpiadorCSV('Datasets/ClaroShop.csv')
limpiador.eliminar_filas_vacias()
limpiador.limpiar_precio()
limpiador.limpiar_descuento()
limpiador.rellenar_comentarios_vacios()
limpiador.eliminar_parentesis_comentarios()
limpiador.quitar_signo_dolar()
limpiador.limpiar_precio_anterior()
limpiador.ordenar_por_producto()
limpiador.eliminar_duplicados()
limpiador.guardar_csv('limpios_ClaroShop.csv')
