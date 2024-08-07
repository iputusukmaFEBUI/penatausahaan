import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
from streamlit_gsheets import GSheetsConnection
from annotated_text import annotated_text

st.sidebar.title("Penatausahaan Aset LMAN")
st.set_page_config(
    page_title="Dasbor Penatausahaan Aset LMAN",
    page_icon="📑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.sidebar.title("Penatausahaan Aset LMAN")

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
st.markdown("Dasbor ini menyajikan informasi penatausahaan aset kelolaan LMAN. yang diadministrasikan oleh unit akuntansi dan pelaporan. Penatausahaan aset kelolaan LMAN dilaksanakan dengan mengacu pada PMK Nomor 144/PMK.06/2020 dan Peraturan Direktur Utama LMAN Nomor 6/LMAN/2021. Nilai aset dan akumulasi penyusutan merupakan posisi per 30 Juni 2024 sebelum akumulasi penyusutan. Total PNBP dan total spending merupakan akumulasi sejak tahun 2016 s.d. 30 Juni 2024. Gross portfolio menunjukkan posisi kelolaan LMAN sebelum akumulasi penyusutan.")
st.markdown("##")

# TOP METRICS
total_porto= int(df["Nilai Aset"].sum())
total_PNBP = int(df["PNBP"].sum())
total_spending = int(df_spend["Spend"].sum())

col = st.columns((4, 4, 4), gap='medium')
with col[0]:
    st.markdown('**:office: Total Gross Portfolio**')
    st.subheader(f"Rp{total_porto:,}")
with col[1]:
    st.markdown('**:chart_with_upwards_trend: Total PNBP**')
    st.subheader(f"Rp{total_PNBP:,}")
with col[2]:
    st.markdown('**:building_construction: Total Spending**')
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
    xaxis=(dict(showgrid=False)),
    yaxis_title=None,
    xaxis_title=None,
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
    xaxis=(dict(showgrid=False)),
    yaxis_title=None,
    xaxis_title=None,
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
    xaxis=(dict(showgrid=False)),
    yaxis_title=None,
    xaxis_title=None,
)



col = st.columns((4, 4, 4), gap='small')
with col[0]:
    st.plotly_chart(fig_top_values_bar,use_container_width=True)
with col[1]:
    st.plotly_chart(fig_top_performers_bar,use_container_width=True)
with col[2]:
    st.plotly_chart(fig_top_spenders_bar,use_container_width=True)


st.markdown("---")

col = st.columns((4, 4, 4), gap='small')
with col[0]:
    st.markdown('**:office: Tabel Gross Portfolio per AsetP**')
    st.dataframe(df_top_values_view,
                 column_order=("Nama Aset","Nilai Aset"),
                 hide_index=True,
                 width=None
                 )


with col[1]:
    st.markdown('**:chart_with_upwards_trend: Tabel PNBP per AsetP**')
    st.dataframe(df_top_performers_view,
                 column_order=("Nama Aset","PNBP"),
                 hide_index=True,
                 width=None
                 )

with col[2]:
    st.markdown('**:building_construction: Tabel Spending per AsetP**')
    st.dataframe(df_top_spenders_view,
                 column_order=("Nama Aset","Spend"),
                 hide_index=True,
                 width=None
                 )
