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




#load data

url = "https://docs.google.com/spreadsheets/d/1br1v4cUjKQ7KCFfHaQfWIix-vw4gtm5-wsoRDAZ9dKQ/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(spreadsheet=url, worksheet="1480371802")

df_top_performers = df.sort_values(by="PNBP",ascending=False)
df_top_performers_view = df_top_performers.loc[:,['Nama Aset','PNBP']]

df_top_values = df.sort_values(by="Nilai Aset",ascending=False)
df_top_values_view = df_top_values.loc[:,['Nama Aset','Nilai Aset']]

df_spend = df
df_spend['Spend']=df_spend['CAPEX']+df_spend['OPEX']
df_top_spenders = df_spend.sort_values(by="Spend",ascending=False)
df_top_spenders_view = df_top_spenders.loc[:,['Nama Aset','Spend']]


# MAIN PAGE
st.header(":bar_chart: Dasbor Penatausahaan Aset Kelolaan")
st.markdown("Nilai gross portfolio merupakan nilai aset per 30 Juni 2024 sebelum akumulasi penyusutan. Total PNBP dan total spending merupakan akumulasi sejak tahun 2016 s.d. 30 Juni 2024.")
st.markdown("##")

# TOP METRICS
total_porto= int(df["Nilai Aset"].sum())
total_PNBP = int(df["PNBP"].sum())
total_spending = int(df_spend["Spend"].sum())

left_column, middle_column, right_column=st.columns(3)
with left_column:
    annotated_text(":office:",("Total Gross Portfolio","","#afa"))
    st.subheader(f"Rp{total_porto:,}")
with middle_column:
    annotated_text(":chart_with_upwards_trend:",("Total PNBP","","#afa"))
    st.subheader(f"Rp{total_PNBP:,}")
with right_column:
    annotated_text(":building_construction:",("Total Spending (CAPEX dan OPEX)","","#afa"))
    st.subheader(f"Rp{total_spending:,}")

st.markdown("---")





# BARCHART

df_top_values_bar = df_top_values_view.reset_index(drop=True)
df_top_values_bar = df_top_values_bar.loc[0:9,['Nama Aset','Nilai Aset']]
df_top_values_bar = df_top_values_bar.sort_values(by="Nilai Aset",ascending=True)
fig_top_values_bar =px.bar(
    df_top_values_bar,
    x="Nilai Aset",
    y="Nama Aset",
    orientation="h",
    title = "<b>Top 10 Gross Values</b>",
    color_discrete_sequence=["#009999"]*len(df_top_values_bar),
      template="plotly_white",
    )
fig_top_values_bar.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)



df_top_performers_bar = df_top_performers_view.reset_index(drop=True)
df_top_performers_bar = df_top_performers_bar.loc[0:9,['Nama Aset','PNBP']]
df_top_performers_bar = df_top_performers_bar.sort_values(by="PNBP",ascending=True)
fig_top_performers_bar =px.bar(
    df_top_performers_bar,
    x="PNBP",
    y="Nama Aset",
    orientation="h",
    title = "<b>Top 10 Revenue Performance</b>",
    color_discrete_sequence=["#0066CC"]*len(df_top_performers_bar),
      template="plotly_white",
    )
fig_top_performers_bar.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)




df_top_spenders_bar = df_top_spenders_view.reset_index(drop=True)
df_top_spenders_bar = df_top_spenders_bar.loc[0:9,['Nama Aset','Spend']]
df_top_spenders_bar = df_top_spenders_bar.sort_values(by="Spend",ascending=True)
fig_top_spenders_bar =px.bar(
    df_top_spenders_bar,
    x="Spend",
    y="Nama Aset",
    orientation="h",
    title = "<b>Top 10 Spending</b>",
    color_discrete_sequence=["#FF9933"]*len(df_top_spenders_bar),
      template="plotly_white",
    )
fig_top_spenders_bar.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)



col = st.columns((4, 4, 4), gap='small')
with col[0]:
    st.plotly_chart(fig_top_values_bar)
with col[1]:
    st.plotly_chart(fig_top_performers_bar)
with col[2]:
    st.plotly_chart(fig_top_spenders_bar)


st.markdown("---")

col = st.columns((4, 4, 4), gap='small')
with col[0]:
    annotated_text(("Daftar lengkap diurutkan menurut nilai aset (Z-A)","","#fea"))
    st.dataframe(df_top_values_view,
                 column_order=("Nama Aset","Nilai Aset"),
                 hide_index=True,
                 width=None
                 )


with col[1]:
    annotated_text(("Daftar lengkap diurutkan menurut PNBP (Z-A)","","#fea"))
    st.dataframe(df_top_performers_view,
                 column_order=("Nama Aset","PNBP"),
                 hide_index=True,
                 width=None
                 )

with col[2]:
    annotated_text(("Daftar lengkap diurutkan menurut jumlah spending (Z-A)","","#fea"))
    st.dataframe(df_top_spenders_view,
                 column_order=("Nama Aset","Spend"),
                 hide_index=True,
                 width=None
                 )
