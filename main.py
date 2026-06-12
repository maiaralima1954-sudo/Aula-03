import streamlit as st
import pandas as pd
from sklearn. linear_model import LinearRegression

st.header('Previsão de vendas')

#Dados: [Investimento em Marketing]-> Faturamento
dados_vendas = pd.DataFrame({
    'investimento': [100,200,300,400,500,600],
    'faturamento':[1200,2500,3200,3400,3600,4000],
})

st.bar_chart(dados_vendas, x = 'investimento', y= 'faturamento')
modelo = LinearRegression()


modelo.fit(dados_vendas[['investimento']], dados_vendas['faturamento'])
media_de_investimento = st.slider('investimento', 0,1000,500)
inv = modelo.predict([[media_de_investimento]])
n = float(inv)

# print(f'{inv:.2f}')
st.success(round(n,2))