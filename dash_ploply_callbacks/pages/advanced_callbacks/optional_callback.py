from dash import Input, Output, get_app, html, no_update, register_page

register_page(__name__)

app = get_app()

layout = html.Div([
    html.Div(
        [
            html.Button(
                id='optional-inputs-button-1', children='Button 1', className='button'
            ),
            html.Div(id='optional-inputs-container'),
            html.Div(id='optional-inputs-output', className='output'),
        ],
        className='container',
    ),
])


@app.callback(
    Output('optional-inputs-container', 'children'),
    Input('optional-inputs-button-1', 'n_clicks'),
    Input('optional-inputs-container', 'children'),
    prevent_initial_call=True,
)
def add_second_button(_, current_children):
    if not current_children:
        return html.Button(
            id='optional-inputs-button-2', children='Button 2', className='button'
        )
    return no_update


@app.callback(
    Output('optional-inputs-output', 'children'),
    Input('optional-inputs-button-1', 'n_clicks'),
    Input('optional-inputs-button-2', 'n_clicks', allow_optional=True),
    prevent_initial_call_output=True,
)
def display_clicks(n_clicks1, n_clicks2):
    return f'Button 1 clicks: {n_clicks1} - Button 2 clicks: {n_clicks2}'
