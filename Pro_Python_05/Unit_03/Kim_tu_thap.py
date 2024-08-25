import streamlit as st

st.title("BÀI THỰC HÀNH VẼ BIỂU ĐỒ KIM TỰ THÁP")
st.write("Thực hiện bởi: ")
#Create list data
chart_data = [
      {"category": "A", "value": 75, "order": 3},
      {"category": "B", "value": 10, "order": 1},
      {"category": "C", "value": 15, "order": 2}
    ]

#convert list data to  dataframe
st.dataframe(chart_data)

st.vega_lite_chart(chart_data, {
    "mark": {"type": "arc", "outerRadius": 80},
  "encoding": {
    "theta": {
      "field": "value", "type": "quantitative",
      "scale": {"range": [2.35619449, 8.639379797]},
    },
    "color": {
      "field": "category", "type": "nominal",
      "scale": {
        "domain": ["A", "B", "C"],
        "range": ["#416D9D", "#674028", "#DEAC58"]
      },
      "legend": {
        "orient": "none",
        "title": "Ghi chú thành phần",
        "columns": 1,
        "legendX": 300,
        "legendY": 80
      }
    },
    "order": {
      "field": "order"
    }
  }
})

