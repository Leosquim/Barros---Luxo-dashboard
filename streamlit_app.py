import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Robô Luxo Dashboard", layout="wide")

st.title("📊 Robô Luxo - Painel de Operações")

st.sidebar.header("Configurações")
saldo_inicial = st.sidebar.number_input("Saldo Inicial ($)", value=1000, step=100)

# Dados fictícios de exemplo
dados = pd.DataFrame({
    "Dia": ["Seg", "Ter", "Qua", "Qui", "Sex"],
    "Lucro": [120, -50, 200, -80, 300]
})

fig = px.line(dados, x="Dia", y="Lucro", markers=True, title="Resultado Diário")
st.plotly_chart(fig, use_container_width=True)

st.metric("💰 Lucro Total", f"${dados['Lucro'].sum():,.2f}")
st.metric("📈 Trades", len(dados))
