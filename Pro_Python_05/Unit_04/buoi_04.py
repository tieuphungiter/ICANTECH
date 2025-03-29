import pandas as pd
import random
import streamlit as st

# 1. Tạo dữ liệu ngẫu nhiên
data = []
for i in range(50):
    id = i + 1
    ten_san_pham = f"Sản phẩm {i+1}"
    so_luong = random.randint(1, 100)
    don_gia = round(random.uniform(10, 1000), 2)
    thanh_tien = so_luong * don_gia
    data.append([id, ten_san_pham, so_luong, don_gia, thanh_tien])

# 2. Tạo DataFrame Pandas
df = pd.DataFrame(data, columns=['id', 'tên sản phẩm', 'số lượng', 'đơn giá', 'thành tiền'])

# 3. Lưu DataFrame vào file CSV
df.to_csv('du_lieu_san_pham.csv', index=False)

# 4. Hiển thị dữ liệu bằng Streamlit
st.title("Dữ liệu sản phẩm")
data = st.dataframe(df)

# Chuẩn bị dữ liệu cho biểu đồ cột
chart_data = df.set_index('tên sản phẩm')[['số lượng', 'đơn giá']]

# Hiển thị biểu đồ cột
st.bar_chart(chart_data)


