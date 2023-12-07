import pandas as pd
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

class ShippingDistributionDashboard:
    def __init__(self, data_path='Datasets/Limpios_ClaroShop.csv'):
        self.df = pd.read_csv(data_path)

        # Inicializar la aplicación Dash con el tema de Bootstrap
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

        # Diseño del dashboard con un gráfico de torta y resumen estadístico
        self.app.layout = self.create_layout()

        # Callbacks
        self.register_callbacks()

    def create_layout(self):
        return dbc.Container(
            [
                html.H1("Distribución del Tipo de Envío en ClaroShop"),
                dbc.Row(
                    [
                        dbc.Col(
                            dcc.Dropdown(
                                id='dropdown-pie-column',
                                options=[{'label': col, 'value': col} for col in self.df.columns],
                                value=self.df.columns[3],  # Asumo que la columna 3 es 'Tipo_de_envio'
                                multi=False,
                            ),
                            width=4,
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id='pie-chart'), width=8),
                        dbc.Col(html.Div(id='summary'), width=4),
                    ]
                ),
            ],
            fluid=True,
        )

    def register_callbacks(self):
        @self.app.callback(
            [Output('pie-chart', 'figure'),
             Output('summary', 'children')],
            [Input('dropdown-pie-column', 'value')]
        )
        def update_pie_chart(selected_column):
            # Crear un gráfico de torta utilizando Plotly Express
            fig = px.pie(self.df, names=selected_column, title=f'Distribución del Tipo de Envío')

            # Calcular el resumen estadístico
            value_counts = self.df[selected_column].value_counts()
            summary_text = f"Resumen de {selected_column}:\n"
            summary_text += value_counts.to_string()

            return fig, summary_text

    def run_server(self):
        # Ejecutar la aplicación
        if __name__ == '__main__':
            self.app.run_server(debug=True)

# Crear una instancia de la clase y ejecutar el servidor
dashboard = ShippingDistributionDashboard()
dashboard.run_server()
