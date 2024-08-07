import streamlit as st
from streamlit_gsheets import GSheetsConnection



st.set_page_config(
    page_title="Dasbor Penatausahaan Aset LMAN",
    page_icon="📑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.sidebar.header("Penatausahaan Aset LMAN")
st.sidebar.write("Divisi Anggaran dan Akuntansi @2024")


# MAIN PAGE
st.header(":bar_chart: Daftar Lengkap Aset Kelolaan LMAN ")
st.markdown("Posisi per 30 Juni 2024")
st.markdown("---")


url = "https://docs.google.com/spreadsheets/d/1br1v4cUjKQ7KCFfHaQfWIix-vw4gtm5-wsoRDAZ9dKQ/edit?usp=sharing"


conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(spreadsheet=url, worksheet="1480371802")

st.dataframe(df)




