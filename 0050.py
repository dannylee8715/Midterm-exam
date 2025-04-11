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
