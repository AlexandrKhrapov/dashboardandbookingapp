import dash
from dash import html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

locations = pd.read_csv('locations.csv')

dash.register_page(__name__, path='/', name="Dashboard")

first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("89%", className="card-title"),
            html.P("Доля заказов доставленных вовремя и в полном объеме (OTIF)"),
        ]
    )
)

second_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("77.5%", className="card-title"),
            html.P("Доля транспортных средств в использовании"),
        ]
    )
)

third_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("2 События", className="card-title"),
            html.P("ТС-N31 требут ремонта, заказ (ID1465148) отменен клиентом"),
        ]
    )
)

fig = px.scatter_mapbox(locations, lat='Lat', lon='Long', zoom=10, size='z', hover_name='Name')
fig.update_layout(mapbox_style="open-street-map")

data_canada = px.data.gapminder().query("country == 'Canada'")
fig2 = px.bar(data_canada, x='year', y='pop', labels={'year': 'minute', 'pop': 'demand'})
fig2.update_xaxes(visible=False, showticklabels=False)

layout = html.Div(children=[
    dbc.Row(
        dbc.Col([
            html.H4("Расположение РЦ"),
            dcc.Graph(figure=fig)
        ])
    ),
    dbc.Row(
        dbc.Col([
            html.H4("Заказы"),
            dcc.Graph(figure=fig2)
        ])
    ),
    dbc.Row([
        dbc.Col(first_card),
        dbc.Col(second_card),
        dbc.Col(third_card),
    ]),
]),
