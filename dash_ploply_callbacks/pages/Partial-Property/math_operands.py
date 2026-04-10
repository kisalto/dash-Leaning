from dash import Input, Output, Patch, callback, dcc, html, register_page
from plotly import graph_objects as go

register_page(__name__)

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]

fig = go.Figure(data=[go.Bar(x=x, y=y)])

layout = html.Div([dcc.Graph(figure=fig, id='increment-example-graph')])


@callback(
    Output('increment-example-graph', 'figure'),
    Input('increment-example-graph', 'clickData'),
    prevent_initial_call=True,
)
def check_selected_data(click_data):
    selected_product = click_data['points'][0]['label']
    patched_figure = Patch()
    if selected_product == 'Product A':
        patched_figure['data'][0]['y'][0] += 1
    elif selected_product == 'Product B':
        patched_figure['data'][0]['y'][0] += 1
    elif selected_product == 'Product C':
        patched_figure['data'][0]['y'][0] += 1
    return patched_figure
