import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np

st.title ("Estatísticas do ano de 2025")

Menu = option_menu(menu_title="Menu",
        options=["Inicio", "Gráficos Estatística", "Gráficos dinâmicos", "Widgets", "Formulário"],
        icons=["house", "bar-chart", "bar-chart-line", "toggles", "bar-chart"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal"
        )

with st.sidebar:
        st.success("**UPLOAD DE DADOS**")
        dados = st.file_uploader(
        "Carregue um ficheiro de dados",
        type=["xlsx", "xls", "csv"]
        )
        
if dados:
        def carregar_dados(dados):
            try:
                df = pd.read_excel(dados)
                return df
            except FileNotFoundError:
                return pd.DataFrame()

        df = carregar_dados(dados)
        st.table(df)

else:
        st.info("Carregue um ficheiro excel para começar")

if menu == "Inicio":
        with st.expander("**Sobre o Instituto Nacional de Estatística**"):
            st.write("Acesse o site www.ine.cv")
            st.image("INE.png")

if menu == "Widgets":
        bt = st.button("Dê um clique!")

        if bt:
            st.info("Clicaste num botão acima!")

        sd = st.slider("Mova o ponto do slider!", min_value=25, \
                       max_value=35, value=30, step=1
                       )

texto = f"Eu tenho {sd} anos!"
st. success(testo)

