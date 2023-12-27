import dash
from geopy.geocoders import Nominatim
from dash import html, callback, Input, Output, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

dash.register_page(__name__, path='/page2', name="Vehicle booking ")

locations = pd.read_csv('locations.csv')

origin_picker_card = dbc.Card([
    dbc.Row(
        dbc.Col(
            html.H3('Точка отправления')
        ),
        justify="center"
    ),
    dbc.Row(
        dbc.Col(
            dcc.Dropdown(
                options=locations['Name'].unique(),
                value='Собственный склад 1',
                multi=False,
                id='Dropdown-origin'
            ),
            width={"size": 6},
            style={"height": "100%"}
        ),
        justify="center"
    ),
])

destination_picker_card = dbc.Card([
    dbc.Row(
        dbc.Col(
            html.H3('Точка назначения')
        ),
        justify="center"
    ),
    dbc.Row(
        dbc.Col(
            dcc.Input(id="Input", type="text", placeholder="Pyatnitskaya St., 3/4, Bldg. 1, Moscow Russia", debounce=True),
            width={"size": 6},
            style={"height": "100%"}
        ),
        justify="center"
    ),
])

layout = html.Div(children=[
    html.Div(
        dbc.Row([
            dbc.Col(
                html.H3("        ")
            )
        ], className="h-15")
    ),
    dbc.Row([
        dbc.Col(
            origin_picker_card
        ),
        dbc.Col(
            destination_picker_card
        )
    ], className="h-35"),
    dbc.Row(
        dbc.Col(
            dcc.Graph(figure={}, id='map')
        )
    ),
])


@callback(
    Output(component_id='map', component_property='figure'),
    [Input(component_id='Dropdown-origin', component_property='value'),
     Input(component_id='Input', component_property='value')]
)
def update_map(locations_filtered, input_adress):
    locations_filtered = locations.query('Name in @locations_filtered')

    app = Nominatim(user_agent="BookingAndDash")
    dest_loc = app.geocode(input_adress)

    locations_filtered.loc[-1] = [input_adress, dest_loc.latitude, dest_loc.longitude, 1, 2]

    fig = px.scatter_mapbox(locations_filtered, lat='Lat', lon='Long', zoom=10, size='z', color='color', hover_name='Name')
    fig.update_layout(mapbox_style="open-street-map")
    return fig
