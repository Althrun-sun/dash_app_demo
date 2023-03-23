import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


def energy_filter(df, energy_type='all'):
    if energy_type == 'all':
        return df
    if energy_type == 'eletric':
        electric_cars_df = df[df['Engine Size (L)'].astype(str).str.contains('Electric')]
        return electric_cars_df
    if energy_type == 'fuel':
        filtered_df = df[df['Engine Size (L)'].notnull()]
        filtered_df = filtered_df[~filtered_df['Engine Size (L)'].astype(str).str.contains('Electric')]
        return filtered_df


def filter_by_0_to_60(df, l, r):

    df['0-60 MPH Time (seconds)'] = pd.to_numeric(df['0-60 MPH Time (seconds)'], errors='coerce')

    filtered_df = df[(df['0-60 MPH Time (seconds)'] >= l) & (df['0-60 MPH Time (seconds)'] <= r)]
    
    return filtered_df  

def filter_by_model(df, model):

    filtered_df = df[df['Car Model'] == model]
    return filtered_df    
def get_data():
    path='car_price.csv'
    return pd.read_csv("EDA/car_price.csv").sort_values('0-60 MPH Time (seconds)')
df = get_data()
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H3("Acceleration vs Price Line Chart"),
            dcc.Graph(id='line_chart'),
        ], width=6),
        dbc.Col([
            html.H3("Car Manufacturers Pie Chart"),
            dcc.Graph(id='pie_chart'),
        ], width=6),
    ]),
    dbc.Row([
        dbc.Col([
            html.H4("Filtered Results (Top 8 Rows)"),
            html.Div(id='filtered_table')
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label("Energy Type"),
            dcc.Dropdown(
                id='energy_type',
                options=[
                    {'label': 'All', 'value': 'all'},
                    {'label': 'Electric', 'value': 'eletric'},
                    {'label': 'Fuel', 'value': 'fuel'},
                ],
                value='all'
            ),
        ], width=4),
        dbc.Col([
            dbc.Label("0-60 Acceleration Range (seconds)"),
            dcc.RangeSlider(
                id='range_slider',
                min=df['0-60 MPH Time (seconds)'].min(),
                max=df['0-60 MPH Time (seconds)'].max(),
                step=0.1,
                value=[df['0-60 MPH Time (seconds)'].min(), df['0-60 MPH Time (seconds)'].max()],
                marks={i: f'{i:.1f}' for i in range(int(df['0-60 MPH Time (seconds)'].min()), int(df['0-60 MPH Time (seconds)'].max()) + 1)},
            ),
        ], width=4),
        dbc.Col([
            dbc.Label("Car Model"),
            dcc.Dropdown(
                id='car_model',
                options=[{'label': model, 'value': model} for model in df['Car Model'].unique()],
                value=None,
            ),
        ], width=4),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Button("Apply Filters", id='apply_filters', color='primary', className='mt-2'),
        ], width=12),
    ]),
])

@app.callback(
    [Output('filtered_table', 'children'),
     Output('line_chart', 'figure'),
     Output('pie_chart', 'figure')],
    [Input('apply_filters', 'n_clicks')],
    [dash.dependencies.State('energy_type', 'value'),
     dash.dependencies.State('range_slider', 'value'),
     dash.dependencies.State('car_model', 'value')]
)
def update_output(n_clicks, energy_type, range_slider, car_model):
    df = get_data()
    filtered_df = energy_filter(df, energy_type)
    filtered_df = filter_by_0_to_60(filtered_df, range_slider[0], range_slider[1])

    if car_model is not None:
        filtered_df = filter_by_model(filtered_df, car_model)

    table = dbc.Table.from_dataframe(filtered_df.head(8), striped=True, bordered=True, hover=True)

    line_chart = px.line(filtered_df, x='0-60 MPH Time (seconds)', y='Price (in USD)', title='Acceleration vs Price', template='plotly_dark')


    pie_chart = px.pie(df, names='Car Make', title='Car Manufacturers', template='plotly_dark')

    return table, line_chart, pie_chart

if __name__ == '__main__':
    app.run_server(debug=True)
