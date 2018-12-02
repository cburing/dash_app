import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os
import plotly

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = [
    ['hello', 'world']
]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

con = os.getenv('DATABASE_URL') if os.getenv('DATABASE_URL') is not None else "postgres://{}:{}@db:5432/{}".format(
    os.getenv('POSTGRES_USER'), os.getenv('POSTGRES_PASSWORD'), os.getenv('POSTGRES_DB'))

print("os.getenv('POSTGRES_PASSWORD')")
print(os.getenv('POSTGRES_PASSWORD'))

print("os.getenv('POSTGRES_USER')")
print(os.getenv('POSTGRES_USER'))

print("os.getenv('POSTGRES_DB')")
print(os.getenv('POSTGRES_DB'))

def get_first_value_from_table(table="person"):
    sql = """
    SELECT name
    FROM {}
    LIMIT 1""".format(table)

    df = pd.read_sql(sql=sql, con=con)

    return html.P(df.iloc[0, 0])


app.layout = html.Div([
    html.H1('Welcome to the app'),
    html.H3('You are successfully authorized'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['A', 'B', 'C']],
        value='A'
    ),
    dcc.Graph(id='graph'),
    get_first_value_from_table(),
    html.P('test')
], className='container')


@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')])
def update_graph(dropdown_value):
    return {
        'layout': {
            'title': 'Graph of {}'.format(dropdown_value),
            'margin': {
                'l': 20,
                'b': 20,
                'r': 10,
                't': 60
            }
        },
        'data': [{'x': [1, 2, 3], 'y': [4, 1, 2]}]
    }


app.scripts.config.serve_locally = True

if __name__ == '__main__':
    app.run_server(debug=True, port=8081, host='0.0.0.0')
