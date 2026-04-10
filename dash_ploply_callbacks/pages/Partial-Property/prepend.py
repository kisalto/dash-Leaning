import random

import plotly.express as px
from dash import Input, Output, Patch, callback, dcc, html, register_page

register_page(__name__)


x_values = [2019, 2020, 2021, 2022, 2023]
y_values = [random.randrange(1, 30, 1) for i in range(5)]

fig = px.bar(x=x_values, y=y_values)

layout = html.Div([
    html.Button('Prepend', id='prepend-new-val'),
    dcc.Graph(figure=fig, id='prepend-example-graph'),
])


@callback(
    Output('prepend-example-graph', 'figure'),
    Input('prepend-new-val', 'n_clicks'),
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks):
    random_value = random.randrange(1, 30, 1)
    patched_figure = Patch()
    patched_figure['data'][0]['x'].prepend(2019 - n_clicks)
    patched_figure['data'][0]['y'].prepend(random_value)
    return patched_figure
