import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import dash_labs as dl
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd



df = pd.read_excel(r"C:\Users\Demirkaya\PycharmProjects\pythonProject1\pages\data.xlsx")
app = dash.Dash(__name__, plugins=[dl.plugins.pages], external_stylesheets=[dbc.themes.FLATLY])

app.layout = html.Div([
    html.H1("Oracle Database Alarm Follower", style={"textAlign": "center"}),
    html.Hr(),
    html.P("Choose an alarm and database:"),
    dcc.Dropdown(id="alarm_choice", options=[{"label": x, "value": x}
                                             for x in sorted(df.ALARM_NAME.unique())],
                 value="ACTIVE SESSION", style={'width': '100%', 'display': 'inline-block'}),
    dcc.Dropdown(id="database_choice", options=[{"label": x, "value": x}
                                                for x in sorted(df.DATABASE_NAME.unique())],
                 value="DB_1", style={'width': '100%', 'display': 'inline-block'}),
    dcc.Graph(id="alarm_graph", figure={})
])

@app.callback(
    Output(component_id="alarm_graph", component_property="figure"),
    Input(component_id="alarm_choice", component_property="value"),
    Input(component_id="database_choice", component_property="value")
)

def interactive_graphing(alarm_value, database_value):
    dff = df.copy()
    dff = dff[df.ALARM_NAME == alarm_value]
    dff = dff[df.DATABASE_NAME == database_value]
    final_fig = px.line(data_frame=dff,
                        x="TIMESTAMP",
                        y=["VALUE", "WARNING", "CRITICAL"],
                        markers=True,
                        color_discrete_sequence=["blue", "yellow", "red"])

    return final_fig


if __name__ == "__main__":
    app.run_server()
