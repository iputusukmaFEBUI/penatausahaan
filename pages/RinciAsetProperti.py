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
st.header(":bar_chart: Rincian Aset Properti Non-Kawasan")
st.markdown("##")

#load data



url = "https://docs.google.com/spreadsheets/d/1br1v4cUjKQ7KCFfHaQfWIix-vw4gtm5-wsoRDAZ9dKQ/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)



df = conn.read(spreadsheet=url, worksheet="Menurut Kategori")

cari_nama = st.selectbox(
    "Nama aset yang akan dilihat datanya",
    options=df["Nama Aset"].unique(),
    index=244,
)

st.markdown("##")

df_tanah = conn.read(spreadsheet=url, worksheet="319942521")
df_tanah = df_tanah.query(
    "`Nama Aset` == @cari_nama"
)
df_bangunan = conn.read(spreadsheet=url, worksheet="1078606570")
df_bangunan = df_bangunan.query(
    "`Nama Aset` == @cari_nama"
)
df_peralatan = conn.read(spreadsheet=url, worksheet="830824723")
df_peralatan = df_peralatan.query(
    "`Nama Aset` == @cari_nama"
)
df_kdp = conn.read(spreadsheet=url, worksheet="1183765865")
df_kdp = df_kdp.query(
    "`Nama Aset` == @cari_nama"
)

nilai_aset = df_tanah['Nilai'].sum()+df_bangunan['Nilai'].sum()+df_peralatan['Nilai'].sum()+df_kdp['Nilai'].sum()
ak_depr = df_bangunan['Ak. Penyusutan'].sum()+df_peralatan['Ak. Penyusutan'].sum()


col = st.columns((1.5,1.5), gap='small')
with col[0]:
    st.markdown(":clipboard: Nilai Aset")
    st.subheader(f"Rp{nilai_aset:,}")
with col[1]:
    st.markdown(":clipboard: Akumulasi Penyusutan")
    st.subheader(f"Rp{ak_depr:,}")

st.markdown("---")




col = st.columns((2.5, 4), gap='small')
with col[0]:
    st.markdown(":round_pushpin: Rincian Tanah")
    st.dataframe(df_tanah[["Uraian BMN","Luas Tanah","Nilai"]],
                hide_index=True,
                width=None,
                column_config={
                    "Luas Tanah":st.column_config.NumberColumn(
                        "Luas Tanah",
                        format="%.2f m2"
                    )})
with col[1]:
    st.markdown(":office: Rincian Bangunan")
    st.dataframe(df_bangunan[["Uraian BMN","Luas Bangunan","Nilai","Ak. Penyusutan","Depreciated"]],
                hide_index=True,
                width=None,
                column_config={
                    "Luas Bangunan":st.column_config.NumberColumn(
                        "Luas Bangunan",
                        format="%.2f m2"
                    ),
                    "Depreciated": st.column_config.ProgressColumn(
                        "Depreciated",
                        help="Persentase terdepresiasi",
                        format="%.2f%%",
                        min_value=0,
                        max_value=100,
                    )}
                )


st.markdown("##")

col = st.columns((2.5, 4), gap='small')
with col[0]:
    st.markdown(":construction: Rincian Konstruksi Dalam Pengerjaan")
    st.dataframe(df_kdp[["Uraian BMN","Nilai"]],
                hide_index=True,
                width=None
                )

with col[1]:
    st.markdown(":hammer_and_wrench: Rincian Peralatan dan Mesin")
    st.dataframe(df_peralatan[["Uraian BMN","Jumlah Unit","Nilai","Ak. Penyusutan","Depreciated"]],
                hide_index=True,
                width=None,
                column_config={
                    "Depreciated": st.column_config.ProgressColumn(
                        "Depreciated",
                        help="Persentase terdepresiasi",
                        format="%.2f%%",
                        min_value=0,
                        max_value=100,
                    )
                }
                )