from dash import Input, Output, callback, dcc, html, register_page

register_page(__name__)

layout = html.Div([
    html.H6('Change the value in the text box to see callbacks in action!'),
    html.Div([
        'Input: ',
        my_input := dcc.Input(value='initial value', type='text')
    ]),
    html.Br(),
    my_Output := html.Div()
])


@callback(
    Output(my_Output, 'children'),
    Input(my_input, 'value'))
def update_output_div(input_value):
    return f'Output: {input_value}'
