import streamlit as st
import pandas as pd
import streamlit_pandas as sp
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from streamlit_gsheets import GSheetsConnection
from annotated_text import annotated_text


st.set_page_config(
    page_title="Dasbor Penatausahaan Aset LMAN",
    page_icon="📑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# MAIN PAGE
st.header(":bar_chart: Data Aset Kelolaan Berupa Kawasan")
st.markdown("##")

#load data

url = "https://docs.google.com/spreadsheets/d/1br1v4cUjKQ7KCFfHaQfWIix-vw4gtm5-wsoRDAZ9dKQ/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)

df_kawasan = conn.read(spreadsheet=url, worksheet="712932311")

cari_kawasan = st.selectbox(
    "Nama aset yang akan dilihat datanya",
    options=df_kawasan["Nama Aset"].unique(),
    index=0,
)

df_view_kawasan = df_kawasan.query(
    "`Nama Aset` == @cari_kawasan"
)

st.markdown("##")

nilai_aset = df_view_kawasan['Nilai'].sum()
ak_depr = df_view_kawasan['Ak. Penyusutan'].sum()

col = st.columns((1.5,1.5), gap='small')
with col[0]:
    st.markdown(":clipboard: Nilai Aset")
    st.subheader(f"Rp{nilai_aset:,}")
with col[1]:
    st.markdown(":clipboard: Akumulasi Penyusutan")
    st.subheader(f"Rp{ak_depr:,}")
st.markdown("##")


st.dataframe(df_view_kawasan,
    column_order=("Kodefikasi Aset","Uraian Kodefikasi","Luas/Jumlah","Satuan","Nilai","Ak. Penyusutan","Depreciated"),
    hide_index=True,
    width=None,
    column_config={
        "Depreciated": st.column_config.ProgressColumn(
        "Depreciated",
        help="Persentase terdepresiasi",
        format="%.2f%%",
        min_value=0,
        max_value=100,   
    )}
)