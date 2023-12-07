import pandas as pd
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

class ProductAnalysisDashboard:
    def __init__(self, data_path='Datasets/Limpios_ClaroShop.csv'):
        self.df = pd.read_csv(data_path)
        self.clean_data()

        # Inicializar la aplicación Dash con el tema de Bootstrap
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

        # Diseño del dashboard
        self.app.layout = self.create_layout()

        # Callbacks
        self.register_callbacks()

    def clean_data(self):
        if self.df['Descuento'].dtype == 'O':
            self.df['Descuento'] = self.df['Descuento'].astype('str').str.rstrip('%').astype('float') / 100.0

    def create_layout(self):
        return dbc.Container(
            [
                html.H1("Análisis de Productos"),

                # Gráfico de barras para el top 15 de productos con más descuento
                self.create_graph('bar-plot-descuento', 'Producto', 'Descuento', 'Top 15 de Productos con Más Descuento'),

                # Gráfico de barras para el top 15 de productos con el precio más bajo
                self.create_graph('bar-plot-precio', 'Producto', 'Precio', 'Top 15 de Productos con Precio Más Bajo'),

                # Gráfico de barras para el top 15 de productos con más comentarios
                self.create_graph('bar-plot-comentarios', 'Producto', 'Comentarios', 'Top 15 de Productos con Más Comentarios'),
            ],
            fluid=True,
        )

    def create_graph(self, graph_id, x_col, y_col, title):
        data = self.df.nlargest(15, y_col)
        return dcc.Graph(
            id=graph_id,
            figure=px.bar(data, x=x_col, y=y_col, title=title)
        )

    def register_callbacks(self):
        pass  # Puedes agregar callbacks aquí si es necesario

    def run_server(self):
        # Ejecutar la aplicación
        if __name__ == '__main__':
            self.app.run_server(debug=True)

# Crear una instancia de la clase y ejecutar el servidor
dashboard = ProductAnalysisDashboard()
dashboard.run_server()
