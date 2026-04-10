import dash_ag_grid as dag
import pandas as pd
from dash import Input, Output, Patch, callback, html, register_page

register_page(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

layout = html.Div([
    html.Button('Delete first row', id='delete-button'),
    html.Button('Reload data', id='reload-button'),
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[{'field': i} for i in df.columns],
        id='table-example-for-delete',
    ),
])


@callback(
    Output('table-example-for-delete', 'rowData'), Input('reload-button', 'n_clicks')
)
def reload_data(n_clicks):
    return df.to_dict('records')


@callback(
    Output('table-example-for-delete', 'rowData', allow_duplicate=True),
    Input('delete-button', 'n_clicks'),
    prevent_initial_call=True,
)
def delete_data(n_clicks):
    patched_table = Patch()
    del patched_table[0]
    return patched_table
