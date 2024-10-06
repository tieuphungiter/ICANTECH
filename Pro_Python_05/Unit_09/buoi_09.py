import streamlit as st
import pandas as pd

st.title('Buoi 09')
st.write("Thực hiện bởi: ")

st.write("Hiển thị bộ dữ liệu gốc: data_09.csv")
data = pd.read_csv('data_09.csv')
st.dataframe(data)

st.write('Hiển thị bộ dữ liệu copy: data_copy = data.copy() ')
data_copy = data.copy()
st.dataframe(data_copy)

st.write("Kiểm tra thông tin dữ liệu")
st.write(data_copy.dtypes)

st.write("Chuẩn hóa bộ dữ liệu Số tầng từ float sang object")
data_copy = data_copy.astype({"Số tầng":"object"})
st.write(data_copy.dtypes)
st.dataframe(data_copy)


st.write("Hiển thị bộ dữ liệu gốc trên tập data_09.csv")
data_2 = pd.read_csv("data_09.csv")
st.dataframe(data_2)

st.write("Kiểm tra dữ liệu trùng lặp trên tập data_09.csv")
st.write(data_2[data_2.duplicated()])
st.write("Kiểm tra dữ liệu trùng lặp trên cột 'Địa chỉ', 'Giấy tờ pháp lý' data_09.csv")
st.write(data_2[data_2.duplicated(subset=['Địa chỉ', 'Giấy tờ pháp lý'])])

st.write("Xử lý dữ liệu trùng lặp")
st.dataframe(data_2.drop_duplicates())