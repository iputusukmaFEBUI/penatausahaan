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
st.markdown("Dasbor ini merupakan dasbor yang menyajikan data dan informasi aset kelolaan LMAN yang disajikan dengan mengacu pada PMK Nomor 144/PMK.06/2020 tentang Pengelolaan Barang Milik Negara oleh Badan Layanan Umum Lembaga Manajemen Aset Negara dan Peraturan Direktur Utama Nomor 6/LMAN/2021 tentang Petunjuk Teknis Penatausahaan Aset Kelolaan Badan Layanan Umum Lembaga Manajemen Aset Negara.")
st.markdown("Data dan informasi yang disajikan pada dasbor ini merupakan data historis yang bersifat kuantitatif dan pendekatan yang digunakan dalam penyajiannya adalah analisis deskriptif. Data dan informasi yang disajikan pada dasbor ini hanya merupakan sebagian kecil alat pendukung pengambilan keputusan manajerial terkait aset kelolaan.")
st.markdown("**Halaman Top Figure** menyajikan total nilai aset, total PNBP dan total spending (_capital expenditure_ dan _operating expenditure_) dan visualisasi atas top-10 atas indikator tersebut. Dasbor ini belum menyajikan informasi yang bersifat _forward-looking_. ")
st.markdown("**Halaman Analitik PNBP** menyajikan total PNBP, rerata PNBP tahunan sepanjang _holding period_, dan _gross income multiplier_ yang merupakan perbandingan antara rerata PNBP tahunan dengan nilai aset sebelum akumulasi penyusutan. Halaman ini juga menyajikan visualisasi atas time-series PNBP dari tahun 2016 s.d. 30 Juni 2024.")
st.markdown("**Halaman Rekap Aset** menyajikan kompilasi data nilai aset, akumulasi penyusutan, PNBP, _capital expenditure_, dan _operating expenditure_ untuk tiap-tiap aset. **Halaman Rincian Aset Kawasan** menyajikan daftar aset per klasifikasi untuk aset-aset kawasan seperti kilang LNG, lapangan golf, dan kawasan komersial sementara **Halaman Rincian Aset Properti** menyajikan daftar aset menurut klasifikasi pada kelompok properti umum non-kawasan.")
st.markdown("---")
st.write("Divisi Anggaran dan Akuntansi -- Direktorat Keuangan dan Dukungan Organisasi")
