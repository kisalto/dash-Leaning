from dash import html, dcc, Input, Output, ctx, callback, register_page

register_page(__name__)

layout = html.Div([
    html.Button('Button 1', id='btn-1-ctx-example'),
    html.Button('Button 2', id='btn-2-ctx-example'),
    html.Button('Button 3', id='btn-3-ctx-example'),
    html.Div(id='container-ctx-example'),
])


@callback(
    Output('container-ctx-example', 'children'),
    Input('btn-1-ctx-example', 'n_clicks'),
    Input('btn-2-ctx-example', 'n_clicks'),
    Input('btn-3-ctx-example', 'n_clicks'),)
def display(btn1, btn2, btn3):
    button_clicked = ctx.triggered_id
    trigger_props = ctx.triggered_prop_ids
    return html.Div([
        dcc.Markdown(
            f'''You last clicked button wih ID {button_clicked} - {trigger_props}
            ''' if button_clicked else '''You haven't clicked any button yet'''
        )
    ])





