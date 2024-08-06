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


#load data

url = "https://docs.google.com/spreadsheets/d/1br1v4cUjKQ7KCFfHaQfWIix-vw4gtm5-wsoRDAZ9dKQ/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(spreadsheet=url, worksheet="1480371802")


# MAIN PAGE
st.header(":bar_chart: Dasbor Penatausahaan Aset Kelolaan")
st.markdown("Nilai gross portfolio merupakan nilai aset per 30 Juni 2024 sebelum akumulasi penyusutan. Total PNBP dan total spending merupakan akumulasi sejak tahun 2016 s.d. 30 Juni 2024.")
st.markdown("##")

# TOP METRICS
total_porto= df['Nilai Aset'].sum()
total_PNBP = df["PNBP"].sum()


st.write(total_porto)
