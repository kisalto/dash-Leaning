from dash import Input, Output, Patch, callback, dcc, html, register_page
from plotly import graph_objects as go

register_page(__name__)

x = ['product A', 'product B', 'product C', 'product D', 'product E']
y = [20, 14, 23, 8]

fig = go.Figure(go.Bar(x=x, y=y))

layout = html.Div([
    html.Button('Reverse Items', id='reverse-button'),
    dcc.Graph(figure=fig, id='reverse-example'),
])


@callback(
    Output('reverse-example', 'figure'),
    Input('reverse-button', 'n_clicks'),
    prevent_initial_call=True,
)
def revert_figure(n_clicks):
    patched_figure = Patch()
    patched_figure['data'][0]['x'].reverse()
    patched_figure['data'][0]['y'].reverse()
    return patched_figure
