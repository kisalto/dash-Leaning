from dash import Input, Output, Patch, callback, dcc, html, register_page

register_page(__name__)

layout = html.Div([
    html.Button('Add options', id='add-options'),
    dcc.RadioItems(
        options={
            'New York City': 'New York City',
            'Montreal': 'Montreal',
            'San Francisco': 'San Francisco',
        },
        value='Montreal',
        id='city-add',
    ),
    html.Div(id='city-output-container'),
])


@callback(Output('city-output-container', 'children'), Input('city-add', 'value'))
def update_output(value):
    return f'You have selected {value}'


@callback(
    Output('city-add', 'options'),
    Input('add-options', 'n_clicks'),
    prevent_initial_call=True,
)
def update_output_2(n_clicks):
    patched_dropdown = Patch()
    european_cities = {'Paris': 'Paris', 'London': 'London', 'berlin': 'Berlin'}
    patched_dropdown.update(european_cities)
    return patched_dropdown
