import streamlit as st
import pandas as pd

st.title('Buoi 06')
st.write("Thực hiện bởi: ")

st.write("Hiển thị bộ dữ liệu gốc: data5.6_1.csv")
data = pd.read_csv('data5.6_1.csv')
st.dataframe(data)

st.write('Hiển thị bộ dữ liệu copy: data_copy = data.copy() ')
data_copy = data.copy()
st.dataframe(data_copy)

st.write("Kiểm tra thông tin dữ liệu")
st.write(data_copy.dtypes)

st.write("Chuẩn hóa bộ dữ liệu race/ethnicity từ float sang object")
data_copy = data_copy.astype({"race/ethnicity":"object"})
st.write(data_copy.dtypes)
st.dataframe(data_copy)


st.write("Hiển thị bộ dữ liệu gốc trên tập data5.6_2.csv")
data_2 = pd.read_csv("data5.6_2.csv")
st.dataframe(data_2)

st.write("Kiểm tra dữ liệu trùng lặp trên tập data5.6_2.csv")
st.write(data_2[data_2.duplicated()])
st.write("Kiểm tra dữ liệu trùng lặp trên cột 'readingscore', 'writingscore' data5.6_2.csv")
st.write(data_2[data_2.duplicated(subset=['readingscore', 'writingscore'])])

st.write("Xử lý dữ liệu trùng lặp")
st.dataframe(data_2.drop_duplicates())