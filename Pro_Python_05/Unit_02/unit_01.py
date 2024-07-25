import pandas as pd

data = pd.read_csv(r"Unit_01\unit_01_weather_data.csv")

# Kiểm tra số dòng hiển thị tối đa của hệ thống
print(pd.options.display.max_rows)
# Hiển thị bộ dữ liệu
print(data)
print(data.info())
