import dash
from dash import html
from dash import dcc
from dash import Input, Output
import pandas as pd
import plotly.express as px
import base64



#data imput

df = pd.read_csv("employees.csv", index_col="_id",
                 parse_dates=['Year Hired'])

app = dash.Dash(__name__)
app.title = "Company!"
image_filename = 'data-analytics.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

#app layout
app.layout = html.Div([
    html.Div([
            html.Img(src='data:data-analytics.png;base64,{}'.format(encoded_image.decode()), className="image"),
            html.Br(),
            html.H1("Welcome to our company!",  className="header-title",),
            html.P("🏬🏬🏬🏬🏬🏬🏬", className="photo"),
            html.P("Welcome to our company statistics"
                   " you can discover our company."
                   " Let's get started!",
                   className="header-description",
                   )], className="header"),
    html.Div([
        html.Div("Select 'x' price:", className="price1"),
        dcc.Dropdown(df.columns, id="my-dropdown", clearable=False),
        html.Br(),
        html.Div("Select 'y' price:", className="price2"),
        dcc.Dropdown(df.columns, id="my-dropdown2", clearable=False), ],
        className="menu"),
    html.Br(),
    dcc.Graph(id="my-graph",),
    ],

)


@app.callback(
    Output(component_id="my-graph", component_property="figure"),
    [Input(component_id="my-dropdown", component_property="value"),
     Input(component_id="my-dropdown2", component_property="value")]

)
def my_update(my_value, my_value2):
    dff = df.copy()
    """print(f"I chose {my_value}")
    print(type(my_value))"""
    fig = px.bar(dff, x=my_value, y=my_value2, title="company")
    return fig





if __name__ == '__main__':
    app.run_server(debug=True)