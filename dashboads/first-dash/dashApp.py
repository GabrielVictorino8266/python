# Primeira dash em Python
# O app rodará em um servidor de endereço http://127.0.0.1:8050/ no navegador

#Para o markdown, é preciso importar Input e Output
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["LEME", "LEME", "LEME", "ARARAS", "ARARAS", "ARARAS"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    dcc.Markdown(
        '''
            # Olá, seja bem-vindo!
        '''
    ),

    dcc.Dropdown(
        id='menus',
        options=[
            {'label': 'Todos', 'value': 'Todos'},
            {'label': 'Leme', 'value': 'Leme'},
            {'label': 'Araras', 'value': 'Araras'},
        ],
        value='Todos',
    ),

        dcc.Graph(
        id='example-graph',
        figure=fig
    ),
])

@app.callback(
    Output('example-graph', 'figure'),
    Input('menus', 'value')
)

def update_output(value):
    if value == 'Araras':
        return px.bar(df[df['City'] == 'ARARAS'], x="Fruit", y="Amount")
    elif value == 'Leme':
        return px.bar(df[df['City'] == 'LEME'], x="Fruit", y="Amount")
    else:
        return px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

if __name__ == '__main__':
    app.run_server(debug=True)