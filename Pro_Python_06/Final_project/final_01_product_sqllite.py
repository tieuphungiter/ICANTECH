import streamlit as st
import sqlite3

# Kết nối với cơ sở dữ liệu SQLite3
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Tạo bảng sản phẩm (nếu chưa có)
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT
)
""")

# Thêm sản phẩm mới
def add_product():
    name = st.text_input("Tên sản phẩm")
    price = st.number_input("Giá bán")
    description = st.text_area("Mô tả")

    if st.button("Thêm"):
        cursor.execute("INSERT INTO products (name, price, description) VALUES (?, ?, ?)", (name, price, description))
        conn.commit()
        st.success("Thêm sản phẩm thành công!")

# Hiển thị danh sách sản phẩm
def show_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    st.write("Danh sách sản phẩm:")
    for product in products:
        st.write(f"- {product[1]}: {product[2]} ({product[3]})")

# Giao diện người dùng
st.title("Website bán hàng")

st.sidebar.title("Giao diện quản lý sản phẩm")
st.write("Học viên: ")
add_product()

st.sidebar.title("Danh sách sản phẩm")
show_products()

# Đóng kết nối cơ sở dữ liệu
conn.close()
