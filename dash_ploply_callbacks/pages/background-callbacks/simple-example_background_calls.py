import time

from dash import (
    Input,
    Output,
    callback,
    html,
    register_page,
    dcc,
)

import plotly.graph_objects as go

def make_progress_graph(progress, total):
    progress_graph = (
        go.Figure(data=[go.Bar(x=[progress])])
        .update_xaxes(range=[0,total])
        .update_yaxes(
            showticklabels=False
        )
        .update_layout(height=100, margin=dict(t=20, b=40))
    )
    return progress_graph


register_page(__name__)

layout = html.Div([
    html.Div([
        html.P(id='paragraph_id', children=['Button not clicked']),
        dcc.Graph(id='progress-bar-graph', figure=make_progress_graph(0, 10)),
    ]),
    html.Button(id='button_id', children='Run Job!'),
    html.Button(id='cancel_button_id', children='Cancel Running Job!'),

])


@callback(
    output=Output("paragraph_id", "children"),
    inputs=Input("button_id", "n_clicks"),
    background=True,
    running=[
        (Output("button_id", "disabled"), True, False),
        (Output("cancel_button_id", "disabled"), False, True),
        (
            Output("paragraph_id", "style"),
            {"visibility": "hidden"},
            {"visibility": "visible"},
        ),
        (
            Output("progress-bar-graph", "style"),
            {"visibility": "visible"},
            {"visibility": "hidden"},
        ),
    ],
    cancel=[Input("cancel_button_id", "n_clicks")],
    progress=Output("progress-bar-graph", "figure"),
    progress_default=make_progress_graph(0, 10))
def update_progress(set_progress, n_clicks):
    total = 10
    for i in range(total):
        time.sleep(0.5)
        set_progress(make_progress_graph(i, 10))

    return f'Clicked {n_clicks} times'
