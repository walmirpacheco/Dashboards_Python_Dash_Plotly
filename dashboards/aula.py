from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("dashboards/vendas.xlsx")
opcoes = list(df['ID Loja'].unique())
opcoes.append("Todas as Lojas")


# Criando gráfico
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráfico com o faturamento de todos os produtos separados por loja'),
    html.Div(children='''
        Obs: Esse gráfico mostra a quantidade de produtos dendidos, não o faturamento.
    '''),
    dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista_lojas'),

    dcc.Graph(
        id='grafico_quantidades_vendas',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)