from dash import html, dcc, Input, Output, callback, register_page

register_page(__name__)

layout = html.Div([
    dcc.Input(id='input-number', type='number', value=1),
    html.Div(id='output-div-err')
])


def update_output_err(err):
#   return f'There was an error processing your input. Error: {err}. Enter another value.'
    return [None]



@callback(
#    Output('output-div-err', 'children'),
    [Output('output-div-err', 'children')],
    Input('input-number', 'value'),
    on_error=update_output_err)
def update_output(value):
    result = 10 / value
#   return f'The result is {result}'
    return [f'The result is {result}']
