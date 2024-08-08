import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
from streamlit_gsheets import GSheetsConnection
from annotated_text import annotated_text

st.set_page_config(
    page_title="Dasbor Penatausahaan Aset LMAN",
    page_icon="📑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.sidebar.header("Penatausahaan Aset LMAN")
st.sidebar.write("Divisi Anggaran dan Akuntansi @2024")




# MAIN PAGE
st.header(":bar_chart: Dasbor Penatausahaan Aset Kelolaan")
st.markdown("Dasbor ini menyajikan informasi penatausahaan aset kelolaan LMAN. yang diadministrasikan oleh unit akuntansi dan pelaporan. Penatausahaan aset kelolaan LMAN dilaksanakan dengan mengacu pada PMK Nomor 144/PMK.06/2020 dan Peraturan Direktur Utama LMAN Nomor 6/LMAN/2021. Nilai aset dan akumulasi penyusutan merupakan posisi per 30 Juni 2024 sebelum akumulasi penyusutan. Total PNBP dan total spending merupakan akumulasi sejak tahun 2016 s.d. 30 Juni 2024. Gross portfolio menunjukkan posisi kelolaan LMAN sebelum akumulasi penyusutan.")
st.markdown("##")
