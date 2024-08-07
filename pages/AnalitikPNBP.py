import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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
st.header(":bar_chart: Analisis Profitabilitas -- Gross Income Multiplier")
st.markdown("Penggunaan Gross Income Multiplier sebagai ukuran profitabilitas aset.")
st.markdown("##")

#load data



url = "https://docs.google.com/spreadsheets/d/1br1v4cUjKQ7KCFfHaQfWIix-vw4gtm5-wsoRDAZ9dKQ/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)

df2 = conn.read(spreadsheet=url, worksheet="1928701477")
#df2["Nilai Aset"] = df2["Nilai Aset"].astype(double)
df2["Gross Income Multiplier"] = df2["Gross Income Multiplier"].astype(float)

# TOP METRICS
top_revenue= int(df2["Total PNBP"].max())
loc_top_revenue = df2.loc[df2['Total PNBP']==top_revenue]
top_average = int(df2["Rerata Tahunan PNBP"].max())
loc_top_average = df2.loc[df2['Rerata Tahunan PNBP']==top_average]
top_gim = float(df2["Gross Income Multiplier"].max())
loc_top_gim = df2.loc[df2['Gross Income Multiplier']==top_gim]

left_column, middle_column, right_column=st.columns(3)
with left_column:
    st.markdown(":chart_with_upwards_trend: Total PNBP Tertinggi")
    st.subheader(f"Rp{top_revenue:,}")
    annotated_text((loc_top_revenue.iloc[0]['Nama Aset'],"","#faa"))
with middle_column:
    st.markdown(":pushpin: Rerata Tahunan Tertinggi")
    st.subheader(f"Rp{top_average:,}")
    annotated_text((loc_top_average.iloc[0]['Nama Aset'],"","#faa"))
with right_column:
    st.markdown(":heavy_check_mark: Gross Income Multiplier Tertinggi")
    st.subheader(f"{top_gim:,.4f} x")
    #st.write(top_gim)
    annotated_text((loc_top_gim.iloc[0]['Nama Aset'],"","#faa"))

st.markdown("---")

st.dataframe(df2,
    column_order=("Nama Aset","Tahun Perolehan","Holding Period","Total PNBP","Rerata Tahunan PNBP","Nilai Aset","Gross Income Multiplier","Time Series"),
    hide_index=True,
    width=None,
    column_config={
        "Tahun Perolehan":st.column_config.NumberColumn(
            "Tahun Perolehan",
            format="%f"
        ),
        "Holding Period":st.column_config.NumberColumn(
            "Holding Period",
            format="%.1f tahun"
        ),   
        "Gross Income Multiplier":st.column_config.NumberColumn(
            "Gross Income Multiplier",
            format="%.4f x"
        ),
        "Nilai Aset":st.column_config.NumberColumn(
            "Nilai Aset",
            format="%,"
        ),
        "Time Series": st.column_config.LineChartColumn(
            "Time Series PNBP",
            help="Time series PNBP 2016 s.d. semester I 2024",
    )}
)
