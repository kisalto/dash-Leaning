from dash import dcc, html, Input, Output, callback, register_page, State, ctx

register_page(__name__)

layout = html.Div([
    html.Button('Botão 1',id='btn-1'),
    html.Button('Botão 2',id='btn-2'),
    html.Button('Botão 3',id='btn-3'),
    html.P('isso é um teste'),
    html.Div(id='btn-information')
])


@callback(
    Output('btn-information', 'children'),
    inputs={
        'all_inputs': {
            'btn1': Input('btn-1', 'n_clicks'),
            'btn2': Input('btn-2', 'n_clicks'),
            'btn3': Input('btn-3', 'n_clicks'),
        }
    },
    prevent_initial_call=True)
def display(all_inputs):
    c = ctx.args_grouping.all_inputs
    if c.btn1.triggered:
        return f'Button 1 clicked {c.btn1.value} times'
    if c.btn2.triggered:
        return f'Button 2 clicked {c.btn2.value} times'
    if c.btn3.triggered:
        return f'Button 3 clicked {c.btn3.value} times'