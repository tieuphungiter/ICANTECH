import streamlit as st
from streamlit_apexjs import st_apexcharts
import random

## Sinh 10 số ngẫu nhiên trong khoảng từ 50 đến 100 (bao gồm cả 0 và 100)
gt_ngau_nhien = []
for i in range(10):
  gt_ngau_nhien.append(random.randint(50, 100))
  
labels_list = [1991, 1992, 1993, 1994, 1995,1996,1997,1998,1999,2000]

options = {
    "chart": {
        "id": "lol",
        "toolbar": {
            "show": False
        }
    },

    "labels": labels_list
    ,
    "legend": {
        "show": True,
        "position": "bottom",
    }
}

options2 = {
    "chart": {
        "id": "lol2",
        "toolbar": {
            "show": False
        }
    },

    "xaxis": {
        "categories": labels_list
    }
    ,
    "legend": {
        "show": True,
        "position": "bottom",
    }
}

options3 = {
    "chart": {
        "id": "lol3",
        "toolbar": {
            "show": False
        }
    },

    "labels": labels_list
    ,
    "legend": {
        "show": True,
        "position": "bottom",
    }
}

series = gt_ngau_nhien
series2 = [{
    "name": 'example',
    "data": gt_ngau_nhien
}]


#thông tin học viên
st.title("Dự án cuối khóa: Phân tích và biểu diễn dữ liệu")
st.write("Học viên: ")


with st.container():
    col1, col2 = st.columns(2)

    with col1:
        st_apexcharts(options, series, 'donut', '100%', 'Title 1')

    with col2:
        st_apexcharts(options2, series2, 'bar', '100%', 'Title 2')

with st.container():
    st_apexcharts(options3, series2, 'line', '700', 'Title 3')