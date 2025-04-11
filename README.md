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
執行後會自動下載 0050.TW 的股價資料，並顯示如下圖表（包含最高與最低點的標示）：

📈 收盤價折線圖（matplotlib 繪製）
🔴 最高點標記
🔵 最低點標記

## 🧾 檔案說明
-0050.py：主程式，畫圖與資料擷取
-README.md：專案說明文件

## 📚 使用套件
-pandas：處理時間序列資料
-matplotlib：畫圖用
-yfinance：抓 Yahoo 股市的資料

## 🪪 授權 License
本專案使用 MIT License，歡迎自由使用與修改。
