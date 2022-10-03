from dash import Dash, html, dcc, Input, Output, State
import pandas as pd
import plotly.express as px


data=pd.read_csv("world_happiness.csv")


app = Dash()

app.layout = html.Div([
        html.H1("Wolrd Happiness Dashboard"),
        html.P(["This dashboard shows the happines score.",
                html.Br(),
               html.A("World Happiness Site", href="https://ourworldindata.org/happiness-and-life-satisfaction", target="_blank")]
        ),
        dcc.RadioItems(id="radio-items",
                       options=data["region"].unique()
                       , value="Eastern Asia"
                       ),
        dcc.Dropdown(id="my-dropdown"),
        dcc.RadioItems(id="my-radio-items",
                       options={
            "happiness_score":"Happiness Score",
            "happiness_rank":"Happiness Rank"
        },
        value="happiness_score"),
        html.Br(),
        html.Button(id="submit-button",n_clicks=0,children="Go!"),
        dcc.Graph(id="graph1"),
        html.Div(id="second-output")
])

@app.callback(
    Output("my-dropdown","options"),
    Output("my-dropdown","value"),
    Input("radio-items", "value")
)
def update_dropdown(selected_region):
    filtered_data = data[data["region"] == selected_region]
    country_options = filtered_data["country"].unique()
    return country_options,country_options[0]

@app.callback(
    Output("graph1","figure"),
    Output("second-output","children"),
    Input("submit-button","n_clicks"),
    State("my-dropdown","value"),
    State("my-radio-items","value"),
)
def update_graph(button_click,country_selection,selected_data):
    filtered_data = data[data["country"]==country_selection]
    line_fig=px.line(filtered_data,x='year',y=selected_data,
                     title=f"{selected_data} in {country_selection}")
    output2 = f"The average {selected_data} for {country_selection} is {filtered_data[selected_data].mean()}"
    return line_fig, output2

if __name__=='__main__':
    app.run_server(debug=True)