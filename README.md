# Midterm-exam 0050 ETF 股價走勢分析

這是一個 Python 專案，用來畫出台灣 0050 ETF 的股價走勢圖，並標出最高點與最低點。

---

## 💻 如何使用

1. 安裝 Python（建議使用 Python 3.x）
2. 安裝所需套件：

pip install matplotlib pandas

kotlin
複製程式碼

3. 把你的股價資料放入一個 pandas 的 DataFrame，命名為 `history_data`，它需要包含「收盤價」和日期，像這樣：

```python
import pandas as pd

# 假設你有這樣的資料
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Close': [120, 122, 118]
}
history_data = pd.DataFrame(data)
history_data['Date'] = pd.to_datetime(history_data['Date'])
history_data.set_index('Date', inplace=True)
執行 0050_stock_trend.py，它會顯示股價走勢圖，並標記出最高點與最低點。

📁 專案檔案說明
0050_stock_trend.py：主程式，負責畫圖

requirements.txt：安裝需要的套件

README.md：這份說明文件

🔧 用到的套件
nginx
複製程式碼
matplotlib
pandas
📝 授權 License
MIT License - 自由使用，但請保留原作者資訊。

yaml
複製程式碼
