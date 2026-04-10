import dash_ag_grid as dag
import pandas as pd
from dash import Input, Output, Patch, callback, html, register_page

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

register_page(__name__)

layout = html.Div([
    html.Button('Delete first row', id='delete-button-1'),
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[{'field': i} for i in df.columns],
        id='table-example-for-delete-1',
    ),
])


@callback(
    Output('table-example-for-delete-1', 'rowData'),
    Input('delete-button-1', 'n_clicks'),
)
def delete_record(n_clicks):
    patched_table = Patch()
    del patched_table[0]
    return patched_table
