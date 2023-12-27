from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc

app = Dash(__name__, pages_folder='pages', use_pages=True, external_stylesheets=[dbc.themes.LUX])

app.layout = html.Div([
    html.Br(),
    html.Div(children=[
        dcc.Link(page['name'], href=page['relative_path'])
        for page in dash.page_registry.values()
    ]),
    dash.page_container
])

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0')
