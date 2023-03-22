from dash import html, dcc
import altair as alt
from vega_datasets import data


# Read in global data
cars = data.cars()

# Setup app and layout/frontend
app = dash.Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.layout = html.Div([
    html.Iframe(
        id='scatter',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    html.Div(id='mean-x-div'),
    html.Br(),
    html.Label([
        'X column',
        dcc.Dropdown(
            id='xcol-widget',
            value='Horsepower',  # REQUIRED to show the plot on the first page load
            options=[{'label': col, 'value': col} for col in cars.columns])]),
    html.Label([
        'Y column',
        dcc.Dropdown(
            id='ycol-widget',
            value='Displacement',  # REQUIRED to show the plot on the first page load
            options=[{'label': col, 'value': col} for col in cars.columns])])])

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Output('mean-x-div', 'children'),
    Input('xcol-widget', 'value'),
    Input('ycol-widget', 'value'))
def plot_altair(xcol, ycol):
    chart = alt.Chart(cars).mark_point().encode(
        x=xcol,
        y=ycol,
        tooltip='Horsepower').interactive()
    return chart.to_html(), f'The mean of {xcol} is {cars[xcol].mean().round(1)}'

if __name__ == '__main__':
    app.run_server(debug=True)