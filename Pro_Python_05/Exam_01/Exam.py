import streamlit as st

# Tiêu đề ứng dụng
st.title("TRANG THÔNG TIN CÁ NHÂN")
st.write("Bài kiểm tra kiến thức streamlit dành cho học viên khóa Python 06")

# Nhập thông tin
with st.form(key="my_form"):
    name = st.text_input("Họ và tên:")
    email = st.text_input("Email:")
    about = st.text_area("Giới thiệu về bản thân:")
    image = st.file_uploader("Upload hình ảnh:", type=["jpg", "png"])
    submitted = st.form_submit_button("Submit")

# Hiển thị thông tin
if submitted:
    st.header("Thông tin của bạn:")
    st.write(f"**Họ và tên:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Giới thiệu:** {about}")
    if image is not None:
        st.image(image)