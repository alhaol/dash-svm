

import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

Fig1= dcc.Graph(
        id='fig1',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': 'Cars'},
            ],
            'layout': {
                'title': 'Basic Dash Example'
            }
        }
    )

Fig2= dcc.Graph(
        id='fig2',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 0, 7, 0], 'type': 'bar', 'name': 'Cars'},
            ],
            'layout': {
                'title': 'Basic Dash Example'
            }
        }
    )
Fig3= dcc.Graph(
        id='fig3',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 0, 7, 0], 'type': 'bar', 'name': 'Cars'},
            ],
            'layout': {
                'title': 'Basic Dash Example'
            }
        }
    )

app.layout = html.Div(children=[
    html.H1(children='Dash Tutorials'),
    Fig1,
    Fig2,
    Fig3
])

# Running the server
if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port='7777')