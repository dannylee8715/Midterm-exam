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