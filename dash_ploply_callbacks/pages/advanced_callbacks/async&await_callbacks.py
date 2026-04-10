import asyncio
import time

from dash import Input, Output, get_app, html, register_page

register_page(__name__, path='/')
app = get_app()


def get_sync_data(iteration):
    time.sleep(1)
    return f'Result ({iteration}) from synchronous API call'


async def get_async_data(iteration):
    await asyncio.sleep(1)
    return f'Result ({iteration}) from asynchronous API call'


layout = html.Div([
    html.H2('synchronous vs. Asynchronous Funcions in Dash'),
    html.Button('Run Sync Tasks', id='Sync-btn', style={'marginRight': '10px'}),
    html.Button('Run Async Tasks', id='Async-btn'),
    html.Hr(),
    html.Div(id='sync-output', style={'color': 'red', 'fontWeight': 'bold'}),
    html.Div(id='async-output', style={'color': 'green', 'fontWeight': 'bold'}),
])


@app.callback(
    Output('sync-output', 'children'),
    Input('Sync-btn', 'n_clicks'),
    prevent_initial_call=True,
)
def sync_callback_example(n_clicks):
    if n_clicks:
        results = [get_sync_data(i) for i in range(5)]
        return html.Div([html.Div(result) for result in results])
    return ''


@app.callback(
    Output('async-output', 'children'),
    Input('Async-btn', 'n_clicks'),
    prevent_initial_call=True,
)
async def update_async_output(n_clicks):
    if n_clicks:
        coros = [get_async_data(i) for i in range(5)]
        results = await asyncio.gather(*coros)
        return html.Div([html.Div(result) for result in results])
    return ''
