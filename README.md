# 0050 ETF 股價走勢分析（0050.py）

這是一個用 Python 製作的股價圖表範例，顯示台灣 0050 ETF 的收盤價，並標示出最高點與最低點。

---

## 🧰 使用方法

### 1️⃣ 安裝需要的 Python 套件

打開終端機（Terminal）或命令提示字元（CMD）執行：

pip install matplotlib pandas


---

### 2️⃣ 準備資料

請先準備一個名為 `history_data` 的 pandas DataFrame，它應該包含「日期」和「收盤價」，像這樣：

```python
import pandas as pd

data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Close': [120, 125, 118]
}
history_data = pd.DataFrame(data)
history_data['Date'] = pd.to_datetime(history_data['Date'])
history_data.set_index('Date', inplace=True)
```
### 3️⃣ 執行 0050.py 程式
python 0050.py
### 📜 程式碼內容（0050.py）
```python
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 設定 matplotlib 使用 SimHei 字型（這是常見的中文支援字型之一）
rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 或者 'SimHei'

# 繪製圖表
history_data['Close'].plot(title="0050.TW 股價走勢", label="收盤價", figsize=(10, 6))

# 標註最高點和最低點
plt.scatter(max_date, max_price, color="red", label="最高點", zorder=5)
plt.scatter(min_date, min_price, color="blue", label="最低點", zorder=5)

# 顯示圖表
plt.legend()
plt.xlabel('日期')
plt.ylabel('價格')
plt.grid(True)
plt.show()
```
### 📂 檔案說明
0050.py：主要繪圖程式

README.md：專案說明文件

### ✅ 結果展示
執行後會顯示 0050 ETF 的收盤價走勢圖，並用紅點標記最高點、藍點標記最低點 📈

### 🪪 License
本專案採用 MIT License，歡迎自由使用與修改。
