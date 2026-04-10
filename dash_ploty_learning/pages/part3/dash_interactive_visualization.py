import json

import pandas as pd
import plotly.express as px
from dash import Input, Output, callback, dcc, html, register_page

register_page(__name__)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'OverflowX': 'scroll'
    }
}

df = pd.DataFrame({
    "x": [1, 2, 1, 2],
    "y": [1, 2, 3, 4],
    "customdata": [1, 2, 3, 4],
    "fruit": ["apple", "apple", "orange", "orange"]
})

# scatter graph vc entra com o DF
# depois as informações que vao em x e y
# o que cada cor quer dizer
# e por fim custom_data pega a posição (x e y)
fig = px.scatter(df, x="x", y="y", color="fruit", custom_data=["customdata"])

# clickmode=''event+select' seleciona o ponto que vc escolheu e deixa os outros gray
fig.update_layout(clickmode='event+select')

# Marker_size é o tamanho do ponto
fig.update_traces(marker_size=20)

layout = html.Div([
    # basicamente settando o grafico
    dcc.Graph(
        id='basic-interactions',
        figure=fig
    ),

    # Aqui ta separando as informaçoes classname row quer dizer que é uma linha
    html.Div(className='row', children=[
        html.Div([
            dcc.Markdown("""
                **Hover Data**

                Mouse over values in the graph.
            """),
            html.Pre(id='hover-data', style=styles['pre'])
        ], className='three columns'),

        html.Div(className='three columns', children=[
            dcc.Markdown(children='''
                **Click Data**

                Click on points in the graph.
            '''),
            html.Pre(id='click-data', style=styles['pre']),
        ]),

        html.Div(className='three columns', children=[
            dcc.Markdown(children='''
                **Selection data**

                Choose the lasso or rectangle tool in the graph's menu
                bar an then select points in the graph.

                Note that if `layout.clickmode = 'event+select'`, selection data also
                accumulates (or un-accumulates) selected data if you hold down the shift
                button while clicking.
            '''),
            html.Pre(id='selected-data', style=styles['pre']),
        ]),

        html.Div(className='three columns', children=[
            dcc.Markdown(children='''
                **Zoom and relayout Data**

                Click and drag on the graph to zoom or click on the zoom
                buttons in the graph's menu bar.
            '''),
            html.Pre(id='relayout-data', style=styles['pre'])
        ]),
    ])
])


# por fim os callbacks onde a magica acontece, json.dumps é para mostrar em json os dados
@callback(
    Output('hover-data', 'children'),
    Input('basic-interactions', 'hoverData'))
def display_hover_data(hoverdata):
    return json.dumps(hoverdata, indent=2)


@callback(
    Output('click-data', 'children'),
    Input('basic-interactions', 'clickData'))
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)


@callback(
    Output('selected-data', 'children'),
    Input('basic-interactions', 'selectedData'))
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)


@callback(
    Output('relayout-data', 'children'),
    Input('basic-interactions', 'relayoutData'))
def display_relayout_data(relayoutdata):
    return json.dumps(relayoutdata, indent=2)
