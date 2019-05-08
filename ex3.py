import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from pandas_datareader import data as pdr
import fix_yahoo_finance as yf

app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children=html.H1('''
        Symbol to graph:
    ''')),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph'),
])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    yf.pdr_override() # <== that's all it takes :-)
    df = pdr.get_data_yahoo(f'{input_data}', 
                           start,
                             end)


    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
        }
    )

# Running the server
if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port='7777')

