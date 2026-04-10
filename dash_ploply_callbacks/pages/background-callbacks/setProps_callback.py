import time
import dash_ag_grid as dag

from dash import Input, Output, html, dcc, set_props, callback, register_page
from plotly.express import data

register_page(__name__)

layout = [
    html.Button(id='button_id', children='Get Data'),
    html.Button(id='cancel_button_id', children='Cancel Running Job!'),
    dag.AgGrid(
        id='ag-grid-updating',
        dashGridOptions={
            'pagination': True
        }
    ),
]


@callback(
    Input("button_id", "n_clicks"),
    background=True,
    running=[
        (Output("button_id", "disabled"), True, False),
        (Output("cancel_button_id", "disabled"), False, True),
    ],
    cancel=[Input("cancel_button_id", "n_clicks")])
def update_progress(n_clicks):
    df = data.gapminder()
    columnsDefs = [{'field': col} for col in df.columns]
    rows_per_step = 100
    total_rows = len(df)

    while total_rows > 0:
        end = len(df) - total_rows + rows_per_step
        total_rows -= rows_per_step
        time.sleep(2)
        set_props(
            'ag-grid-updating',
            {'rowData': df[:end].to_dict('records'), 'columnDefs': columnsDefs}
        )


