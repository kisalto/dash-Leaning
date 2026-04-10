from dash import Input, Output, ctx, html, dcc ,callback, register_page
import plotly.express as px
import plotly.graph_objects as go

register_page(__name__)

layout = html.Div([
    html.Button('Draw Graph', id='draw'),
    html.Button('Reset Graph', id='reset'),
    dcc.Graph(id='graph')
])


@callback(
    Output('graph', 'figure', allow_duplicate=True),
    Input('reset', 'n_clicks'),
    prevent_initial_call=True)
def update_graph(n_clicks):
    return go.Figure()
    

@callback(
    Output('graph', 'figure'),
    Input('draw', 'n_clicks'),
    prevent_initial_call=True)
def draw_graph(n_clicks):
    df = px.data.iris()
    return px.scatter(df, x=df.columns[0], y=df.columns[1])
