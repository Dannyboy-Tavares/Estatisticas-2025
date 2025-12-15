import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np

Menu = option_menu(
        "Navegação", ["Iniciar", "Estatística", "Pesquisar", "Dados"],
        menu_icon="cast",
        icons=["house", "bar-chart", "search", "graph-up-arrow"],
        default_index=0
    )
st.title ("Estatísticas do ano de 2025")
