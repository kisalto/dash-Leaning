import time
from datetime import datetime

from dash import Input, Output, callback, get_app, html, register_page

register_page(__name__)
app = get_app()

layout = html.Div([
    html.Button('execute callbacks', id='button_2'),
    html.Div(id='first_output_2', children='callback not executed'),
    html.Div(id='second_output_2', children='callback not executed'),
    html.Div(id='third_output_2', children='callback not executed'),
    html.Div(id='fourth_output_2', children='callback not executed'),
])


@callback(
    Output('first_output_2', 'children'),
    Output('second_output_2', 'children'),
    Input('button_2', 'n_clicks'),
    prevent_initial_call=True,
)
def first_callback(n):
    now = datetime.now().strftime('%H:%M:%S')
    return ['in the first callback it is ' + now, 'In the first callback it is ' + now]


@callback(
    Output('third_output_2', 'children'),
    Input('second_output_2', 'children'),
    prevent_initial_call=True,
)
def second_callback(n):
    time.sleep(2)
    now = datetime.now().strftime('%H:%M:%S')
    return 'in the second callback it is ' + now


@callback(
    Output('fourth_output_2', 'children'),
    Input('first_output_2', 'children'),
    Input('third_output_2', 'children'),
    prevent_initial_call=True,
)
def third_callback(n, m):
    time.sleep(2)
    now = datetime.now().strftime('%H:%M:%S')
    return 'in the third callback it is ' + now
