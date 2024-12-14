import streamlit as st
import time

# Tạo tiêu đề và mô tả cho ứng dụng
st.title("Đăng ký tài khoản")
st.write("Vui lòng điền đầy đủ thông tin bên dưới")

# Tạo các trường nhập liệu
with st.form(key='my_form'):
    username = st.text_input("Tài khoản")
    password = st.text_input("Mật khẩu", type='password')
    confirm_password = st.text_input("Nhập lại mật khẩu", type='password')
    full_name = st.text_input("Tên người dùng")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Đăng ký")

# Kiểm tra và xử lý khi người dùng nhấn nút đăng ký
if submitted:
    # Ở đây bạn sẽ thêm logic kiểm tra dữ liệu nhập vào, ví dụ:
    # - Kiểm tra mật khẩu có trùng khớp không
    # - Kiểm tra định dạng email
    # - Lưu trữ thông tin vào cơ sở dữ liệu (nếu có)

    # Thêm progress bar để tạo hiệu ứng chờ đợi
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)

    st.success("Đăng ký thành công!")


