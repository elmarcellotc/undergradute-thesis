from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__)

# This is the header of all document

header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                dbc.Col(html.H3("Add DHUB Logo"))
            )
        ]
    )
)


app.layout = html.Div([
    header
])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=2023)