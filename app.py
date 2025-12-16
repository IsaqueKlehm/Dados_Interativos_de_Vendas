import pandas as pd
import streamlit as st
import requests
import plotly.express as px

st.set_page_config(layout='wide')

# Função para formatar valores
def formata_numero(valor, prefixo=''):
    for unidade in ['', 'Mil']:
        if valor < 1000:
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /= 1000
    return f'{prefixo} {valor:.2f} Milhões'

st.title('DASHBOARD DE VENDAS')

# Importando API
url = 'https://labdados.com/produtos'
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())

# Convertendo datas
dados['Data da Compra'] = pd.to_datetime(dados['Data da Compra'], format='%d/%m/%Y')


# Receita por estado
receita_estados = dados.groupby('Local da compra')[['Preço']].sum()
receita_estados = (
    dados.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']]
    .merge(receita_estados, left_on='Local da compra', right_index=True)
    .sort_values('Preço', ascending=False)
)

# Receita Mensal
receita_mensal = (
    dados.set_index('Data da Compra')
    .groupby(pd.Grouper(freq='M'))['Preço']
    .sum()
    .reset_index()
)

receita_mensal['Ano'] = receita_mensal['Data da Compra'].dt.year
receita_mensal['Mes'] = receita_mensal['Data da Compra'].dt.month_name()

# Receita por categoria
receita_categorias = (
    dados.groupby('Categoria do Produto')[['Preço']]
    .sum()
    .sort_values('Preço', ascending=False)
)


vendedores = pd.DataFrame(dados.groupby('Vendedor')['Preço'].agg(['sum', 'count']))


# Mapa de receita
fig_mapa_receita = px.scatter_geo(
    receita_estados,
    lat='lat',
    lon='lon',
    scope='south america',
    size='Preço',
    template='seaborn',
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon': False},
    title='Receita por estado',
)

# Receita Mensal
fig_receita_mensal = px.line(
    receita_mensal,
    x='Mes',
    y='Preço',
    markers=True,
    color='Ano',
    line_dash='Ano',
    title='Receita Mensal',
)

fig_receita_mensal.update_layout(yaxis_title='Receita')

# Receita por estado
fig_receita_estados = px.bar(
    receita_estados.head(),
    x='Local da compra',
    y='Preço',
    text_auto=True,
    title='Top estados (receita)',
)

fig_receita_estados.update_layout(yaxis_title='Receita')

# Receita por categoria
fig_receita_categorias = px.bar(
    receita_categorias,
    y='Preço',
    text_auto=True,
    title='Receita por categoria',
)

fig_receita_categorias.update_layout(yaxis_title='Receita')




aba1, aba2, aba3 = st.tabs(['Receita', 'Quantidade de Vendas', 'Vendedores'])

with aba1:        
    coluna1, coluna2 = st.columns(2)

    with coluna1:
        st.metric('Receita', formata_numero(dados['Preço'].sum(), 'R$'))
        st.plotly_chart(fig_mapa_receita, use_container_width=True)
        st.plotly_chart(fig_receita_estados, use_container_width=True)

    with coluna2:
        st.metric('Quantidade de Vendas', formata_numero(dados.shape[0]))
        st.plotly_chart(fig_receita_mensal, use_container_width=True)
        st.plotly_chart(fig_receita_categorias, use_container_width=True)

with aba2:        
    coluna1, coluna2 = st.columns(2)

    with coluna1:
        st.metric('Receita', formata_numero(dados['Preço'].sum(), 'R$'))
    with coluna2:
        st.metric('Quantidade de Vendas', formata_numero(dados.shape[0]))

with aba3:        
    qtd_vendedores = st.number_input('Quantidade de vendedores', 2, 10, 5) # vai aparecer 2 de 10 vendedores, e vai poder alterar entre 2 até 10
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita', formata_numero(dados['Preço'].sum(), 'R$'))
        fig_receita_vendedores = px.bar(
            vendedores[['sum']].sort_values('sum', ascending=False).head(qtd_vendedores),
            x = 'sum',
            y = vendedores[['sum']].sort_values('sum', ascending=False).head(qtd_vendedores).index,
            text_auto = True, # Vai colocar um texto automatico em cada barra
            title = f'Top {qtd_vendedores} vendedores (receita)'
        )
        st.plotly_chart(fig_receita_vendedores)
    with coluna2:
        st.metric('Quantidade de Vendas', formata_numero(dados.shape[0]))
        fig_vendas_vendedores = px.bar(
            vendedores[['count']].sort_values('count', ascending=False).head(qtd_vendedores),
            x = 'count',
            y = vendedores[['count']].sort_values('count', ascending=False).head(qtd_vendedores).index,
            text_auto = True, # Vai colocar um texto automatico em cada barra
            title = f'Top {qtd_vendedores} vendedores (quantidade de vendas)'
        )
        st.plotly_chart(fig_vendas_vendedores)

