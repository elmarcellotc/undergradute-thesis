import dash
from dash import html
from dash import dcc

motivation = html.Div(children=[
    html.H1(children='Motivation'),

    html.Div(children='''This working papers got the following objectives:'''),
    html.Div(children='''1 - Replicate the findings of Hidalgo and Hausmann with ecuadorian data'''),
    html.Div(children='''2 - Provide Ecuadorian data of the research and how it is connected as a network'''),
    html.Div(children='''3 - Test if the research network shows the same results as the industrial network'''),
    html.Div(children='''4 - Merge both networks by suing public NLP libraries'''),
    html.Div(children='''3 - Test some graph theory common variables, as predictors of the industrial share''')

])