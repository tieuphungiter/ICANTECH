import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

st.title("BÀI THỰC HÀNH PYTHON PRO 05 BUỔI 02")

st.write('Thực hiện bởi: ')

data=pd.read_csv('unit_02_data.csv')
st.write("Hiển thị dữ liệu với: st.table(data) ")
st.table(data)
st.write("Hiển thị dữ liệu với: st.dataframe(data)")
st.dataframe(data)
st.write("Hiển thị dữ liệu với: st.write(data)")
st.write(data)