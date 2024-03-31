import streamlit as st
from streamlit_gsheets import GSheetsConnection
from streamlit_dynamic_filters import DynamicFilters


st.set_page_config(

    layout="wide"
)

st.title("Daftar Aset Kelolaan LMAN")
#st.sidebar.success("pilih tab")

url = "https://docs.google.com/spreadsheets/d/1br1v4cUjKQ7KCFfHaQfWIix-vw4gtm5-wsoRDAZ9dKQ/edit?usp=sharing"


conn = st.connection("gsheets", type=GSheetsConnection)

#st.write(st.secrets['connections'])
data = conn.read(spreadsheet=url, worksheet="1468705168")

dynamic_filters = DynamicFilters(df=data, filters=['Nama Aset'])
#with st.sidebar:
dynamic_filters.display_filters()
dynamic_filters.display_df()
#st.dataframe(data)

git+https://github.com/streamlit/gsheets-connection
