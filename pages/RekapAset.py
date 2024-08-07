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

# TOP METRICS
nilai_aset= int(df["Nilai Aset"].sum())
ak_penyusutan = int(df["Ak. Penyusutan"].sum())
nilai_bersih = int(df["Nilai Bersih"].sum())

col = st.columns((4, 4, 4), gap='medium')
with col[0]:
    st.markdown('**:chart_with_upwards_trend: Nilai Aset**')
    st.subheader(f"Rp{nilai_aset:,}")
with col[1]:
    st.markdown('**:clipboard: Total PNBP**')
    st.subheader(f"Rp{ak_penyusutan:,}")
with col[2]:
    st.markdown('**:pushpinn: Total Spending**')
    st.subheader(f"Rp{nilai_bersih:,}")

st.markdown("---")

st.dataframe(df)




