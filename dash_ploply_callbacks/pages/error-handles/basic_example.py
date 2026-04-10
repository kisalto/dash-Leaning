from dash import html, dcc, Input, Output, callback, register_page

register_page(__name__)

layout = html.Div([
    dcc.Input(id='input-number', type='number', value=1),
    html.Div(id='output-div')
])


def custom_err_handler(err):
    print(f'The app raised the following exception: {err}')


@callback(
    Output('output-div', 'children'),
    Input('input-number', 'value'),
    on_error=custom_err_handler)
def update_output(value):
    result = 10 / value
    return f'The result is {result}'
