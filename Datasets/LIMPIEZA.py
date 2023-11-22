import pandas as pd
import re

class LimpiadorCSV:
    def __init__(self, archivo):
        self.df = pd.read_csv(archivo)

    def eliminar_filas_vacias(self):
        self.df = self.df.dropna()

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

    def eliminar_parentesis_comentarios(self):
        def _eliminar_parentesis_y_convertir(texto):
            if isinstance(texto, str):
                numero = re.sub(r'[()]', '', texto)
                return int(numero)
            return texto
        self.df['Comentarios'] = self.df['Comentarios'].apply(_eliminar_parentesis_y_convertir)

    def eliminar_columna(self, nombre_columna):
        self.df = self.df.drop(nombre_columna, axis=1)

    def quitar_signo_dolar(self):
        self.df['Precio anterior'] = self.df['Precio anterior'].astype(str).str.replace('$', '')

    def guardar_csv(self, archivo_salida):
        self.df.to_csv(archivo_salida, index=False)


# Uso de la clase
limpiador = LimpiadorCSV('ClaroShop.csv')
limpiador.eliminar_filas_vacias()
limpiador.limpiar_precio()
limpiador.limpiar_descuento()
limpiador.eliminar_parentesis_comentarios()
limpiador.eliminar_columna('Unnamed: 0')
limpiador.quitar_signo_dolar()
limpiador.guardar_csv('limpios_ClaroShop.csv')
