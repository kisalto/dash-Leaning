import dash
from dash import Input, Output, callback, dcc, html

dash.register_page(__name__)

layout = html.Div([
    dcc.Input(id='num-multi', type='number', value=5, min=-10, max=10),
    html.Table([
        html.Tr([html.Td(['x', html.Sup(2)]), html.Td(id='square')]),
        html.Tr([html.Td(['x', html.Sup(3)]), html.Td(id='cube')]),
        html.Tr([html.Td(['2', html.Sup('x')]), html.Td(id='twos')]),
        html.Tr([html.Td(['3', html.Sup('x')]), html.Td(id='threes')]),
        html.Tr([html.Td(['x', html.Sup('x')]), html.Td(id='x^x')]),
    ]),
])


@callback(
    Output('square', 'children'),
    Output('cube', 'children'),
    Output('twos', 'children'),
    Output('threes', 'children'),
    Output('x^x', 'children'),
    Input('num-multi', 'value')
)
def callback_a(x):
    if x is None:
        return "", "", "", "", ""
    return x**2, x**3, 2**x, 3**x, x**x
