import dash
from dash import dcc, html
from dash import dash_table
import plotly.express as px
import dataset_parser as parser
import plots

DATASET='../datasets/chronic_kidney_disease_full.arff'
ATTR_LABELS='../datasets/attributes_labeling.csv'

# Load data array
data_array = parser.read_arff_data(DATASET)
# Load attribute information array
attribute_info_array = parser.read_labeling_data(ATTR_LABELS)
# Make Data Frame
df = parser.make_dataframe(data_array, attribute_info_array)
table = plots.get_data_table(df)
# Initialize Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign': 'center'}),

    dcc.Dropdown(
        id='dropdown-table-sort',
        options=[{'label': col, 'value': col} for col in df.columns],  # List of column names
        value='class',  # Default value
        style={'width': '50%', 'margin': 'auto'}
    ),

    dcc.Graph(
        id='table-content',
        figure=table,
        config={'displayModeBar': False}  # Hide the toolbar for the table
    ),

    # Dropdown for selecting column names dynamically
    dcc.Dropdown(
        id='dropdown-selection',
        options=[{'label': col, 'value': col} for col in df.columns],  # List of column names
        value='age',  # Default value
        style={'width': '50%', 'margin': 'auto'}
    ),

    # Graph to display data based on selected column
    dcc.Graph(id='graph-content'),

    # Dropdown for selecting x-axis attribute for the scatter plot
    dcc.Dropdown(
        id='dropdown-x-axis',
        options=[{'label': col, 'value': col} for col in df.columns],  # List of column names
        value='age',  # Default value for x-axis
        style={'width': '50%', 'margin': 'auto'}
    ),

    # Dropdown for selecting y-axis attribute for the scatter plot
    dcc.Dropdown(
        id='dropdown-y-axis',
        options=[{'label': col, 'value': col} for col in df.columns],  # List of column names
        value='bp',  # Default value for y-axis
        style={'width': '50%', 'margin': 'auto'}
    ),

    # Graph to display scatter plot based on selected x and y columns
    dcc.Graph(id='scatter-plot')
])

# Define callback to update the table based on selected sorting column
@app.callback(
    dash.dependencies.Output('table-content', 'figure'),
    [dash.dependencies.Input('dropdown-table-sort', 'value')]
)
def update_table(selected_column):
    # Sort the DataFrame based on the selected column
    df_sorted = df.sort_values(by=selected_column)

    # Create a Plotly table with the sorted DataFrame
    table_fig = plots.get_data_table(df_sorted)
    return table_fig


# Define callback to update the scatter plot based on selected x and y attributes
@app.callback(
    dash.dependencies.Output('scatter-plot', 'figure'),
    [
        dash.dependencies.Input('dropdown-x-axis', 'value'),
        dash.dependencies.Input('dropdown-y-axis', 'value')
    ]
)
def update_scatter_plot(x_column, y_column):
    # Create a scatter plot based on the selected x and y columns
    fig = px.scatter(df, x=x_column, y=y_column, title=f'Scatter Plot of {x_column} vs {y_column}')
    return fig


# Define callback to update the graph based on selected column
@app.callback(
    dash.dependencies.Output('graph-content', 'figure'),
    [dash.dependencies.Input('dropdown-selection', 'value')]
)
def update_graph(selected_column):
    df_sorted = df.sort_values(by=selected_column)
    # Create a simple plot for the selected column
    fig = px.histogram(df_sorted, x=selected_column, title=f'Distribution of {selected_column}')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
