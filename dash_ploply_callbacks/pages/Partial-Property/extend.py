from dash import Input, Output, Patch, callback, dcc, html, register_page
from plotly import graph_objects as go

register_page(__name__)

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]

additional_products_x = ['Product D', 'Product E', 'Product F']
additional_products_y = [10, 24, 8]

fig = go.Figure(data=[go.Bar(x=x, y=y)])

layout = html.Div([
    html.Button('Update products', id='additional-products'),
    dcc.Graph(figure=fig, id='extend-example'),
])


@callback(
    Output('extend-example', 'figure'),
    Input('additional-products', 'n_clicks'),
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks):
    if n_clicks % 2 != 0:
        patched_figure = Patch()
        patched_figure['data'][0]['x'].extend(additional_products_x)
        patched_figure['data'][0]['y'].extend(additional_products_y)
        return patched_figure
    else:
        return fig
