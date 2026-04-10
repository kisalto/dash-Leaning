import dash_ag_grid as dag
from dash import Input, Output, Patch, callback, dcc, html, register_page
from plotly import graph_objects as go

register_page(__name__)

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]

table_data = [{'Product': x_value, 'Value': y_value} for x_value, y_value in zip(x, y)]


additional_products_x = ['Product D', 'Product E', 'Product F']
additional_products_y = [10, 21, 8]

fig = go.Figure(data=[go.Bar(x=x, y=y)])

layout = html.Div([
    html.Button('Update Products', id='add-additional-products'),
    dcc.Graph(figure=fig, id='multiple-outputs-fig'),
    dag.AgGrid(
        rowData=table_data,
        columnDefs=[{'field': i} for i in ['Product', 'Value']],
        id='multiple-outputs-table',
    ),
])


@callback(
    Output('multiple-outputs-fig', 'figure'),
    Output('multiple-outputs-table', 'rowData'),
    Input('add-additional-products', 'n_clicks'),
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks):
    if n_clicks % 2 != 0:
        patched_figure = Patch()
        patched_table = Patch()

        additional_table_data = [
            {'Product': x_value, 'Value': y_value}
            for x_value, y_value in zip(additional_products_x, additional_products_y)
        ]

        patched_table.extend(additional_table_data)

        patched_figure.data[0].x.extend(additional_products_x)
        patched_figure.data[0].y.extend(additional_products_y)

        return patched_figure, patched_table
    else:
        return fig, table_data
