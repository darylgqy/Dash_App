import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import datetime
import pandas as pd
#for compatibility between datareader and pandas
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
df = web.DataReader("F", 'morningstar', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)
app = dash.Dash()

app.layout = html.Div(children = [
    html.H1("Dash for graph tutorials"),
    dcc.Graph(id = 'example',
                figure = {
                    'data': [
                        {'x': df.index, 'y': df.Close, 'type':'line', 'name':'stock'},
                    ],
                    'layout': {
                        'title': 'Stock Price'
                    }
                })
    ])

if __name__ == "__main__":
    app.run_server(debug = True)
