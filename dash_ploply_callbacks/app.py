import os
from dash import (
    Dash,
    DiskcacheManager,
    Input,
    Output,
    callback,
    dcc,
    html,
    no_update,
    page_container,
    page_registry,
)
from dash.exceptions import PreventUpdate

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Setup background callback manager
import diskcache
cache = diskcache.Cache('./cache')
background_callback_manager = DiskcacheManager(cache)

app = Dash(__name__, external_stylesheets=external_stylesheets, use_pages=True, background_callback_manager=background_callback_manager)
# register_page("começo", )

app.layout = (
    html.Div([
        html.Div([
            dcc.Dropdown(
                options=[
                    {'label': page['name'], 'value': page['relative_path']}
                    for page in page_registry.values()
                ],
                id='page-dropdown',
                value=None,
            ),
        ]),
        html.Hr(),
        dcc.Location(id='page-location', refresh='callback-nav'),
        page_container,
        html.Hr(),
        html.P('Enter a composite number to see its prime factors:'),
        dcc.Input(id='num', type='number', debounce=True, min=2, step=1),
        html.P(id='err', style={'color': 'red'}),
        html.P(id='out'),
    ]),
)


@callback(Output('out', 'children'), Output('err', 'children'), Input('num', 'value'))
def show_factors(num):
    if num is None:
        raise PreventUpdate

    factors = prime_factors(num)
    if len(factors) == 1:
        return no_update, f'{num} is prime!.'.format(num)

    return '{} is {}'.format(num, ' * '.join(str(f) for f in factors)), ''


@callback(
    Output('page-location', 'href', allow_duplicate=True),
    Input('page-dropdown', 'value'),
    prevent_initial_call=True,
)
def switch_page(value):
    return value


def prime_factors(num):
    c = 2
    n, i, out = num, 2, []
    while i * i <= n:
        if n % i == 0:
            n = int(n / i)
            out.append(i)
        else:
            i += 1 if i == c else 2
    out.append(n)
    return out


if __name__ == '__main__':
    app.run(debug=True)
