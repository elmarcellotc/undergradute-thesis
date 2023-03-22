import dash
from dash import html, dcc
from pages.motivation import motivation

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    dcc.Tabs(
        
        id='alignment-tabs', value='what-is',
        children=[
            dcc.Tab(
                label='Motivation',
                value='motivation',
                children=html.Div(className='motivtion-tab', children=motivation)
            )
        ]
    )
])