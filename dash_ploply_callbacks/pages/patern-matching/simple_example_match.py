from dash import (
    MATCH,
    Input,
    Output,
    Patch,
    State,
    callback,
    dcc,
    get_app,
    html,
    register_page,
)

register_page(__name__)
app = get_app()

layout = html.Div([
    html.Button('Add Filter', id='dynamic-add-filter-btn', n_clicks=0),
    html.Div(id='dynamic-dropdown-container-div', children=[]),
])


@callback(
    Output('dynamic-dropdown-container-div', 'children'),
    Input('dynamic-add-filter-btn', 'n_clicks'),
)
def display_dropdown(n_clicks):
    patched_children = Patch()

    new_element = html.Div([
        dcc.Dropdown(
            ['NYC', 'MTL', 'LA', 'TOKYO'],
            id={'type': 'city-dynamic-dropdown', 'index': n_clicks},
        ),
        html.Div(id={'type': 'city-dynamic-output', 'index': n_clicks}),
    ])
    patched_children.append(new_element)
    return patched_children


@callback(
    Output({'type': 'city-dynamic-output', 'index': MATCH}, 'children'),
    Input({'type': 'city-dynamic-dropdown', 'index': MATCH}, 'value'),
    State({'type': 'city-dynamic-dropdown', 'index': MATCH}, 'id'),
)
def display_output(value, id):
    return html.Div(f'dropdown {id["index"]} = {value}')
