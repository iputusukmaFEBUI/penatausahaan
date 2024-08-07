import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_gsheets import GSheetsConnection
from annotated_text import annotated_text


st.set_page_config(
    page_title="Dasbor Penatausahaan Aset LMAN",
    page_icon="📑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# MAIN PAGE
st.header(":bar_chart: Rincian Aset Properti Non-Kawasan")
st.markdown("##")

#load data



url = "https://docs.google.com/spreadsheets/d/1br1v4cUjKQ7KCFfHaQfWIix-vw4gtm5-wsoRDAZ9dKQ/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(spreadsheet=url, worksheet="1480371802")

df_properti = conn.read(spreadsheet=url, worksheet="893621252")

df_view_properti = df_kawasan.query(
    "`Nama Aset` == @cari_properti"
)

st.markdown("##")

nilai_aset = df_view_properti['Nilai'].sum()
ak_depr = df_view_properti['Ak. Penyusutan'].sum()

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
