import dash 
import dash_core_components as dcc 
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd 
import yahoo_fin.stock_info as si
import yfinance as yf

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)


ticker_data = si.get_data("AAPL", "2020-07-01", "2020-07-20",True).head(10)

fig = px.bar(ticker_data, x="Symbol", y="close", color="Name", barmode= "group")

app.layout = html.Div([
    html.H1("Simple Stock Analysis"),
    html.Div([
        html.Div([
            dcc.Input(id='stock_ticker', type='text', placeholder='Ticker Symbol'),
            html.Button(id='submit',n_clicks=0, children = 'Submit'),
        ])
    ], className="six columns"),
    
    html.Br(),
    html.Hr(),

    html.Div([
    html.H3("Top Gainers of the Day"),
    dcc.Graph(
        id= "ticker_graph",
        figure= fig
    )
    ], style={'text-align': 'center'}),

    
])

@app.callback(
     Output('ticker_graph', 'figure'),
     [Input('submit',',n_clicks')],
     [State('stock_ticker', 'value')]
 )

def return_graph(n_clicks, ticker):
    if ticker != "":
        ticker_data= si.get_data(ticker,"2020-07-01", "2020-07-20", "1d")
        graph = px.line(ticker_data, x= ticker_data.index.value, y="close")
        return graph
    else:
        return None


# def update_graph(ticker):
#     if ticker != None:
#         ticker_data = si.get_data(ticker,start_date="2020-07-01", end_date="2020-07-20", interval='1d')
#         ticker_df = pd.DataFrame(ticker_data)
#         fig = plt.Line2D()
#         return fig
#     else:
#         ticker_data = si.get_data("AAPL",start_date="2020-07-01", end_date="2020-07-20", interval='1d')
#         ticker_df = pd.DataFrame(ticker_data)
#         fig = px.line(ticker_df)
#         return fig


if __name__ == '__main__':
    app.run_server(debug=True)
