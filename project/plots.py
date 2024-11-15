import plotly.graph_objects as go

def get_data_table(data_frame):
    table = go.Figure(data=[go.Table(
        header=dict(values=list(data_frame.columns),
                    fill_color='#222222',  font=dict(color='white', size=12),
                    align='center'),

        cells=dict(values=[data_frame[col] for col in data_frame.columns],
                   fill_color=['#444444', '#333333', '#444444', '#333333', '#444444','#333333',
                               '#444444', '#333333', '#444444', '#333333', '#444444','#333333',
                               '#444444', '#333333', '#444444', '#333333', '#444444','#333333',
                               '#444444', '#333333', '#444444', '#333333', '#444444','#333333', '#444444'],
                   font=dict(color='white', size=11),
                   align='center')
    )])

    map_color = {"ckd":"green", "nockd":"red", "BORDERLINE":"blue"}

    data_frame["class"] = data_frame["class"].map(map_color)

    cols_to_show = ["name", "value", "output"]


    return table


def get_table(df):
    cell_colors = []
    for value in df['class']:
        if value == 'ckd':
            cell_colors.append('green')
        else:
            cell_colors.append('red')

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=df.columns,
            fill_color='gray',  # Dark header background
            font=dict(color='white'),
            align='center'
        ),
        cells=dict(
            values=[df[col] for col in df.columns],
            fill_color=[['#333333'], ['#222222'], ['#333333'], ['#222222'],
                        ['#333333'], ['#222222'], ['#333333'], ['#222222'],
                        ['#333333'], ['#222222'], ['#333333'], ['#222222'],
                        ['#333333'], ['#222222'], ['#333333'], ['#222222'],
                        ['#333333'], ['#222222'], ['#333333'], ['#222222'],
                        ['#333333'], ['#222222'], ['#333333'], ['#222222'],cell_colors],  # Dark-themed cells with color based on class
            font=dict(color='white'),  # White text for contrast
            align='center'
        )
    )])

    # Update layout for a dark background
    fig.update_layout(
        plot_bgcolor='black',  # Dark background
        paper_bgcolor='black',  # Dark paper background
        title='Classified Data Table',
        title_font=dict(color='white'),
        font=dict(color='white')
    )

    # Show the table
    return fig