# 🚀 Bitcoin Sentiment vs Trader Performance Analysis

<div align="center">

### 📊 Analyzing the Impact of Bitcoin Market Sentiment on Trader Performance

</div>

---

## 📌 Project Overview

This project explores the relationship between **Bitcoin market sentiment** and **trader performance** using:

| Dataset | Description |
|---|---|
| 📈 Hyperliquid Historical Data | Historical trader activity and trading performance |
| 📊 Fear & Greed Index | Daily Bitcoin market sentiment classification |

The goal of this analysis is to identify how market psychology influences:

- 💰 Trader profitability  
- 📈 Trading volume  
- ⚠️ Risk-taking behavior  
- 🔄 Buy/Sell activity  
- 🧠 Market participation patterns  

> 📍 Complete preprocessing, analysis workflow, and implementation logic are available in `analysis.py`.

---

# 🛠️ Tech Stack

<div align="center">

| Technology | Usage |
|---|---|
| 🐍 Python | Core Programming |
| 🐼 Pandas | Data Analysis |
| 📊 Matplotlib | Data Visualization |
| 🎨 Seaborn | Statistical Visualization |

</div>

---

# ⚙️ Analysis Workflow

| Step | Description |
|---|---|
| 1️⃣ | Data Cleaning |
| 2️⃣ | Date Formatting |
| 3️⃣ | Dataset Merging |
| 4️⃣ | Exploratory Data Analysis |
| 5️⃣ | Sentiment-Based Analysis |
| 6️⃣ | Trader Performance Analysis |
| 7️⃣ | Profitability Analysis |
| 8️⃣ | Correlation Analysis |
| 9️⃣ | Visualization & Insight Generation |

---

# 📈 Visual Analysis

---

## 📊 Market Sentiment Distribution

![Market Sentiment Distribution](images/sentiment_distribution.png)

🔍 Shows the distribution of Fear and Greed sentiment categories across the dataset.

---

## 💰 Average Trader Profit by Sentiment

![Average Trader Profit](images/pnl_by_sentiment.png)

🔍 Compares average trader profitability during different sentiment conditions.

---

## 📈 Trading Volume Analysis

![Trading Volume](images/trading_volume.png)

🔍 Highlights how market sentiment impacts trading activity and participation.

---

## 🔄 Buy vs Sell Activity

![Buy vs Sell Activity](images/buy_sell_analysis.png)

🔍 Compares Buy and Sell behavior during Fear and Greed market conditions.

---

## 🏆 Top 10 Most Profitable Traders

![Top Traders](images/top_traders.png)

🔍 Identifies traders with the highest cumulative profitability.

---

## 🔥 Correlation Heatmap

![Correlation Heatmap](images/correlation_heatmap.png)

🔍 Displays relationships between important trading metrics such as:
- Execution Price
- Trade Size
- Closed PnL
- Fees
- Sentiment Value

---

# ▶️ Setup & Execution

## 📦 Install Required Libraries

```bash
pip install pandas matplotlib seaborn
```

---

## ▶️ Run the Project

```bash
python analysis.py
```

---

# 📁 Repository Structure

```text
bitcoin-sentiment-trader-analysis/
│
├── analysis.py
├── README.md
│
└── images/
    ├── sentiment_distribution.png
    ├── pnl_by_sentiment.png
    ├── trading_volume.png
    ├── buy_sell_analysis.png
    ├── top_traders.png
    └── correlation_heatmap.png
```

---

# 🔍 Key Insights

| 📌 Area | Insight |
|---|---|
| 💰 Profitability | Greed periods generally showed higher average profitability |
| ⚠️ Volatility | Fear periods were associated with unstable trader performance |
| 📈 Trading Activity | Trading volume increased significantly during bullish sentiment |
| 🔄 Trading Behavior | Buy activity dominated during Greed phases |
| 🧠 Trader Psychology | Market sentiment strongly influenced trader confidence |
| 🏆 Trader Performance | A small group of traders contributed a large portion of total profits |
| 📊 Strategy Optimization | Sentiment analysis can improve trade timing and risk management |
| ⚡ Risk Appetite | Traders appeared more aggressive during optimistic market conditions |

---

# 🎯 Final Outcome

✅ Successfully analyzed the relationship between:

- Bitcoin market sentiment  
- Trader profitability  
- Trading activity  
- Market participation  
- Risk-taking behavior  

The project demonstrates how sentiment indicators can help improve:

- 📈 Trading strategies  
- ⚠️ Risk management  
- 🧠 Market understanding  
- ⏱️ Trade timing decisions  

---

# ⚠️ Dataset Upload Note

The original datasets were not uploaded directly to this repository because the file sizes exceeded GitHub's upload limitations.

To keep the repository lightweight and easier to review, the original dataset links are provided below.

---

## 📈 Hyperliquid Historical Trader Dataset

https://drive.google.com/file/d/1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs/view?usp=sharing

---

## 📊 Bitcoin Fear & Greed Index Dataset

https://drive.google.com/file/d/1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf/view?usp=sharing
