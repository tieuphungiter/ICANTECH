import streamlit as st
import pandas as pd
import numpy as np


data = pd.read_csv("pyramid.csv")
chart_data = pd.DataFrame(data)

st.dataframe(chart_data)
st.vega_lite_chart(data, {
    "mark": {"type": "arc"},
    "encoding": {
        "theta": {
            "field":"value", "type": "quantitative",
            "scale":{"range": [2.35, 8.63]}
        },
        "color": {
            "field":"category", "type": "nominal",
            "scale":{
                "domain": ["A", "B", "C"],
                "range": ["#416D9D", "#674028","#DEAC58"]
            },
            "legend": {
                "orient": "right","title": "Chú thích màu sắc",
            }},
        "order": {"field": "order"}
}
})