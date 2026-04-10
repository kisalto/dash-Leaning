from dash import Input, Output, Patch, callback, dcc, html, register_page
from plotly import graph_objects as go

register_page(__name__)

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]

fig = go.Figure(data=[go.Bar(x=x, y=y)])

layout = html.Div([
    html.Button('Update Products', id='update-product-d-e'),
    dcc.Graph(figure=fig, id='preappend-example-graph'),
])


@callback(
    Output('preappend-example-graph', 'figure'),
    Input('update-product-d-e', 'n_clicks'),
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks):
    if n_clicks % 2 != 0:
        patched_figures = Patch()
        patched_figures.data[0].x.prepend('Product D')
        patched_figures.data[0].y.prepend(34)
        patched_figures.data[0].x.append('Product E')
        patched_figures.data[0].y.append(34)
        return patched_figures
    else:
        return fig
