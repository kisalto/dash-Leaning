from dash import Input, Output, Patch, callback, dcc, html, register_page
from plotly import graph_objects as go

register_page(__name__)

x = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
y = [20, 14, 23, 8]


fig = go.Figure(data=[go.Bar(x=x, y=y)])

layout = html.Div([
    html.Button('update products', id='additional-products-insert'),
    dcc.Graph(figure=fig, id='insert-example'),
])


@callback(
    Output('insert-example', 'figure'),
    Input('additional-products-insert', 'n_clicks'),
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks):
    if n_clicks % 2 != 0:
        patched_figure = Patch()
        patched_figure['data'][0]['x'].insert(1, 'Product B')
        patched_figure['data'][0]['y'].insert(1, 10)
        return patched_figure
    else:
        return fig
