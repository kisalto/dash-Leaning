from dash import Input, Output, Patch, callback, dcc, html, register_page

register_page(__name__)

layout = html.Div([
    html.Button('Remove items', id='remove-button', type='submit'),
    dcc.Checklist(id='checklist-remove-items'),
])


@callback(
    Output('checklist-remove-items', 'options'),
    Input('checklist-remove-items', 'value'),
    Input('remove-button', 'n_clicks'),
    Input('checklist-remove-items', 'options'),
)
def remove_records(items, n_clicks, opt):
    if not n_clicks:
        return [
            'Boston',
            'Montreal',
            'New York',
            'Toronto',
            'San Francisco',
            'Vancouver',
        ]
    elif n_clicks % 2 == 0:
        return opt
    else:
        patched_list = Patch()
        for x in items:
            patched_list.remove(x)
        return patched_list


@callback(
    Output('remove-button', 'children'),
    Input('remove-button', 'n_clicks'),
    prevent_initial_call=True,
)
def change_button_name(n_clicks):
    if n_clicks % 2 != 0:
        return 'Deletando...'
    else:
        return 'Remove items'
