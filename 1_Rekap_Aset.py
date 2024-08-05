import streamlit as st
from streamlit_gsheets import GSheetsConnection
#from streamlit_dynamic_filters import DynamicFilters

st.set_page_config(
    layout="wide"
)

st.title("Daftar Aset Kelolaan LMAN")
#st.sidebar.success("pilih tab")

url = "https://docs.google.com/spreadsheets/d/1br1v4cUjKQ7KCFfHaQfWIix-vw4gtm5-wsoRDAZ9dKQ/edit?usp=sharing"


conn = st.connection("gsheets", type=GSheetsConnection)

#st.write(st.secrets['connections'])
data = conn.read(spreadsheet=url, worksheet="1468705168")

def validate():
    if '1' not in st.session_state.multiselect:
        st.session_state.multiselect = ['FY 202']

reportingperiod = st.multiselect(
    "Select the time to maturity:",
    options = ("FY 2016","FY 2017","FY 2018",'FY 2019',"FY 2020","FY 2021","FY 2022","FY 2023","SMT I 2024"),
    default="1",
    on_change=validate,
    key='multiselect'
)


data_selection = data.query(
    "ReportingPeriod == @reportingperiod"
)



plotly_figure = px.area(data_frame = data_selection,
x = df_selection['Periode Laporan'], y=data_selection['Total Nilai'], color = data_selection['ReportingPeriod'], template='seaborn', line_shape='spline',
title= 'Yield of INDOGB, Maturity in Month(s)', color_discrete_sequence=px.colors.qualitative.Pastel
)


#dynamic_filters = DynamicFilters(df=data, filters=['Nama Aset'])
#with st.sidebar:
#dynamic_filters.display_filters()
#dynamic_filters.display_df()
st.dataframe(data)

