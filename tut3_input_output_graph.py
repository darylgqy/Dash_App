import dash
import pandas as pd
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import datetime
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
#for compatibility between datareader and pandas
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web


app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='''
        Symbol to graph:
    '''),
    dcc.Input(id='input', value = '', type='text'),
    html.Div(id='output-graph'),
])

@app.callback(
    Output(component_id = 'output-graph', component_property = 'children'),
    [Input(component_id = 'input', component_property = 'value')]
)
def update_graph(input_data):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(input_data, 'morningstar', start, end)
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    df = df.drop("Symbol", axis=1)

    return dcc.Graph(id = 'example',
                figure = {
                    'data': [
                        {'x': df.index, 'y': df.Close, 'type':'line', 'name':'stock'},
                    ],
                    'layout': {
                        'title': input_data
                    }
                })
if __name__ == "__main__":
    app.run_server(debug = True)
