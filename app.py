from dash import Dash, html, dcc
import dash
import os

app = Dash(__name__)

app.layout = html.Div([
    html.H3("IM DEAD")
])

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)), host='0.0.0.0')
