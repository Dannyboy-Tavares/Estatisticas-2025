import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np

st.title ("Estatísticas do ano de 2025")

Menu = option_menu(menu_title="Menu",
        options=["Inicio", "Gráficos Estatística", "Gráficos dinâmicos", "Widgets", "Formulário"],
        icons=["house", "bar-chart", "bar-chart-line", "toggles", "bar-chart"],
        menu_icon="cast"
        default_index=0,
        orientation="horizontal"
    )

