# 0050 ETF 股價趨勢分析（Python + Yahoo Finance）

本專案是用 Python 畫出台灣 0050 ETF（股票代碼：0050.TW）最近 6 個月的股價走勢圖，並標示出最高與最低點。

---

## 🚀 功能說明

- 使用 `yfinance` 自動下載 Yahoo 股市資料
- 顯示最近半年收盤價走勢
- 標示出最高價與最低價（含日期與數值）
- 中文圖表標籤支援

---

## 📦 安裝方式

打開終端機（Terminal）或命令提示字元（CMD）：

```bash
pip install yfinance pandas matplotlib
```
## ▶️ 執行程式
```bash
python 0050.py
```
## 📜 程式碼內容（0050.py）
<details>
<summary><h2>點我展開0050.py</h2></summary>
    
```python
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import yfinance as yf

# 下載 0050 的歷史資料（近 6 個月）
ticker = yf.Ticker("0050.TW")
history_data = ticker.history(period="6mo")

# 如果找不到資料就停止
if history_data.empty:
raise Exception("找不到 0050.TW 的歷史資料，請確認網路或股票代碼是否正確。")

# 計算最高與最低點
max_price = history_data['Close'].max()
min_price = history_data['Close'].min()
max_date = history_data['Close'].idxmax()
min_date = history_data['Close'].idxmin()

# 設定 matplotlib 支援中文字型
rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 或 'SimHei'
rcParams['axes.unicode_minus'] = False  # 解決負號亂碼

# 繪製圖表
history_data['Close'].plot(title="0050.TW 股價走勢（近6個月）", label="收盤價", figsize=(10, 6))

# 標註最高點與最低點
plt.scatter(max_date, max_price, color="red", label=f"最高點：{max_price:.2f}", zorder=5)
plt.scatter(min_date, min_price, color="blue", label=f"最低點：{min_price:.2f}", zorder=5)

# 顯示圖表
plt.legend()
plt.xlabel('日期')
plt.ylabel('價格（TWD）')
plt.grid(True)
plt.tight_layout()
plt.show()
```
</details>

### 執行後會自動下載 0050.TW 的股價資料，並顯示如下圖表（包含最高與最低點的標示）：

📈 收盤價折線圖（matplotlib 繪製）

🔴 最高點標記

🔵 最低點標記

(0050曲線圖.jpg)

## 🧾 檔案說明
- 0050.py：主程式，畫圖與資料擷取
- README.md：專案說明文件

## 📚 使用套件
- pandas：處理時間序列資料
- matplotlib：畫圖用
- yfinance：抓 Yahoo 股市的資料

## 🪪 授權 License
本專案使用 MIT License，歡迎自由使用與修改。
