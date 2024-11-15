import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from dash import Dash, html, dcc, callback, Output, Input


def get_data_table(data_frame):
    # Create a Plotly table
    fig = go.Figure(data=[go.Table(
        header=dict(values=data_frame.columns),  # Header from DataFrame columns
        cells=dict(values=[data_frame[col] for col in data_frame.columns])  # Data from DataFrame
    )])

    # Show the table
    return fig

def get_attribute_histogram(data_frame, attribute_to_display):
    fig = px.histogram(data_frame, x= attribute_to_display)
    return fig

def get_dataset_histogram(data_frame):

    figures = []
    for attribute in data_frame.columns:
        figure = get_attribute_histogram(data_frame, attribute)
        figure.show()
        figures.append(figure)

    cols = 4
    rows = len(figures)// cols

    fig = make_subplots(
        rows=rows, cols=cols,
        subplot_titles= data_frame.columns,
        shared_xaxes=True,  # Optionally share x-axis for consistency
        shared_yaxes=True   # Optionally share y-axis for consistency
    )

    fig.show()