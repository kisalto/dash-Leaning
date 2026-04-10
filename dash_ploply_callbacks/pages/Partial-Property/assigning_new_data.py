import plotly.express as px
from dash import Input, Output, Patch, callback, dcc, html, register_page

register_page(__name__)

df = px.data.election()[:20]
fig = px.bar(df, x='district')

layout = html.Div([
    dcc.Dropdown(['Coderre', 'Joly', 'Bergeron'], id='Candidate-select', value='Joly'),
    dcc.Graph(figure=fig, id='new-data-graph'),
])


@callback(Output('new-data-graph', 'figure'), Input('Candidate-select', 'value'))
def update_figure(value):
    patched_figure = Patch()
    patched_figure['data'][0]['y'] = df[value].values
    return patched_figure
