import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, dash_table

class DiscountAnalysisDashboard:
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
        top_30_descuento = self.df.nlargest(30, 'Descuento')

        return dbc.Container(
            [
                html.H1("Top 30 de Productos con Mayor Descuento"),

                # Tabla interactiva con el top 30 de productos con mayor descuento
                self.create_data_table(top_30_descuento),
            ],
            fluid=True,
        )

    def create_data_table(self, data):
        return dash_table.DataTable(
            id='datatable',
            columns=[
                {'name': 'Producto', 'id': 'Producto'},
                {'name': 'Precio Anterior', 'id': 'Precio_anterior'},
                {'name': 'Precio Actual', 'id': 'Precio'},
                {'name': 'Descuento', 'id': 'Descuento', 'format': {'specifier': '.2%'}}
            ],
            data=data.to_dict('records'),
            style_table={'height': '500px', 'overflowY': 'auto'},
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            row_selectable="multi",
            selected_rows=[],
        )

    def register_callbacks(self):
        pass  # Puedes agregar callbacks aquí si es necesario

    def run_server(self):
        # Ejecutar la aplicación
        if __name__ == '__main__':
            self.app.run_server(debug=True)

# Crear una instancia de la clase y ejecutar el servidor
dashboard = DiscountAnalysisDashboard()
dashboard.run_server()
