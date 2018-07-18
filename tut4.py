import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components
import plotly
import random
import plotly.graph_objs as go
#container e.g list with limi\ted size (max length)
from collections import deque

X = deque(maxlen = 20)
Y = deque(maxlen = 20)
X.append(1)
Y.append(1)

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id = 'live-graph', animate = True),
        dcc.Interval(
            id = 'graph-update',
            interval = 1000
        ),
    ]
) 

@app.callback(Output('live-graph', 'figure'),
                events = [Event('graph-update', 'interval')])
def update_graph():
    X.append(X[-1]+1)
    Y.append(Y[-1]+(Y[-1]*random.uniform(-0.1, 0.1))

    data = go.Scatter(
        x = list(X),
        y = list(Y),
        name = 'Scatter',
        mode = 'lines+markers '
        )

    return {'data': [data], 'layout': go.layout(xaxis = dict(range = [min(X), max(X)]),
                                                yaxis = dict(range = [min(Y), max(Y)]),)}

if __name__ == '__main__':
    app.run_server(debug=True)