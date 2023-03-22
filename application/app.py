import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

# Tabs:

from pages.motivation import motivation


DEFAULT_STROKE_WIDTH = 3  # gives line width of 2^3 = 8

DEFAULT_IMAGE_PATH = "assets/segmentation_img.jpg"

SEG_FEATURE_TYPES = ["intensity", "edges", "texture"]

# the number of different classes for labels
NUM_LABEL_CLASSES = 5
DEFAULT_LABEL_CLASS = 0
class_label_colormap = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2"]
class_labels = list(range(NUM_LABEL_CLASSES))
# we can't have less colors than classes
assert NUM_LABEL_CLASSES <= len(class_label_colormap)

# Font and background colors associated with each theme
text_color = {"dark": "#95969A", "light": "#595959"}
card_color = {"dark": "#2D3038", "light": "#FFFFFF"}

features_dict = {}

external_stylesheets = [dbc.themes.BOOTSTRAP, "static/segmentation-style.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, use_pages=True)

server = app.server
app.title = "Ecuadorian Productive Networks"


# Header
header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.Img(
                            id="logo",
                            src="static/dhub-logo.jpg",
                            height="30px",
                        ),
                        md="auto",
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                [
                                    html.H3("ECUADORIAN PRODUCTIVE NETWORKS"),
                                    html.P("Marcello Coletti"),
                                ],
                                id="app-title",
                            )
                        ],
                        md=True,
                        align="center",
                    ),
                ],
                align="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.NavbarToggler(id="navbar-toggler"),
                            dbc.Collapse(
                                dbc.Nav(
                                    [
                                        dbc.NavItem(
                                            dbc.Button(page['name'], outline=True,
                                                       color='primary', href=page['relative_path'],
                                                       style={"text-transform": "none"},
                                                       external_link=True)
                                        ) for page in dash.page_registry.values()
                                    ],
                                    navbar=True,
                                ),
                                id="navbar-collapse",
                                navbar=True,
                            )
                        ],
                        md=2,
                    ),
                ],
                align="center",
            ),
        ],
        fluid=True,
    ),
    dark=True,
    color="dark",
    sticky="top",
)


app.layout = html.Div(
    [
        header,
        dash.page_container
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port = 2023)