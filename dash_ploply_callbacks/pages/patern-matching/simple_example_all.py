from dash import (
    ALL,
    Input,
    Output,
    Patch,
    callback,
    dcc,
    get_app,
    html,
    register_page,
)

register_page(__name__)
app = get_app()

layout = html.Div([
    html.Button('Add Filter', id='add-filter-btn', n_clicks=0),
    html.Div(id='dropdown-container-div', children=[]),
    html.Div(id='dropdown-container-output-div'),
])


@callback(
    Output('dropdown-container-div', 'children'), Input('add-filter-btn', 'n_clicks')
)
def display_dropdown(n_clicks):
    patched_children = Patch()
    new_dropdown = dcc.Dropdown(
        ['NYC', 'MTL', 'LA', 'TOKYO'],
        id={'type': 'city-filter-dropdown', 'index': n_clicks},
    )
    patched_children.append(new_dropdown)
    return patched_children


@callback(
    Output('dropdown-container-output-div', 'children'),
    Input({'type': 'city-filter-dropdown', 'index': ALL}, 'value'),
)
def display_output(values):
    return html.Div([
        html.Div(f'Dropdown {i + 1} = {values}') for (i, values) in enumerate(values)
    ])
