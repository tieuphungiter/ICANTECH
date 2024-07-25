import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#pip install matplotlib
import seaborn as sns
#pip install seaborn

st.title("Dự án phân tích dữ liệu bán hàng")
st.write("Thực hiện bởi: ")
# Đọc dữ liệu
data = pd.read_csv("sales_data.csv")

# Tạo giao diện
st.title("Báo cáo Bán Hàng")

# Hiển thị dữ liệu dạng bảng
st.dataframe(data)

# Tạo biểu đồ doanh thu theo thời gian
st.subheader("Doanh thu theo thời gian")
fig, ax = plt.subplots()
sns.lineplot(x="Year", y="Profit", data=data, ax=ax)
st.pyplot(fig)

# Tạo biểu đồ phân bố doanh thu theo sản phẩm
st.subheader("Phân bố doanh thu theo sản phẩm")
fig, ax = plt.subplots()
sns.barplot(x="Country", y="Profit", data=data, ax=ax)
st.pyplot(fig)

# Cho phép người dùng chọn sản phẩm để xem chi tiết
selected_product = st.selectbox("Chọn sản phẩm", data["Product"].unique())
filtered_data = data[data["Product"] == selected_product]
st.dataframe(filtered_data)
