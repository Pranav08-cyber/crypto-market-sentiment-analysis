# 🚀 Bitcoin Sentiment vs Trader Performance Analysis

<div align="center">

### 📊 Analyzing the Impact of Bitcoin Market Sentiment on Trader Performance

</div>

---

# 📌 Project Overview

This project explores the relationship between **Bitcoin market sentiment** and **trader performance** using:

| Dataset | Description |
|---|---|
| 📈 Hyperliquid Historical Data | Historical trader activity and trading performance |
| 📊 Fear & Greed Index | Daily Bitcoin market sentiment classification |

The objective of this analysis is to understand how market psychology influences:

- 💰 Trader profitability  
- 📈 Trading volume  
- ⚠️ Risk-taking behavior  
- 🔄 Buy/Sell activity  
- 🧠 Market participation patterns  

> 📍 Complete preprocessing, analysis workflow, and implementation details are available in `analysis.py`.

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

<div align="center">

```text
        ┌────────────────────┐
        │   Load Datasets    │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │   Data Cleaning    │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Date Formatting    │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │   Merge Datasets   │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Exploratory Data   │
        │     Analysis       │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Sentiment-Based    │
        │     Analysis       │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Trader Performance │
        │     Analysis       │
        └─────────┬──────────┘
                  │
                  ▼
        ┌────────────────────┐
        │ Visualization &    │
        │ Insight Generation │
        └────────────────────┘
```

</div>

---

# 📈 Visual Analysis

---

## 📊 Market Sentiment Distribution

<img width="630" height="531" alt="sentiment_distribution" src="https://github.com/user-attachments/assets/2360988b-e740-4622-8a31-e8be2a587324" />


🔍 Shows the distribution of Fear and Greed sentiment categories across the dataset.

---

## 💰 Average Trader Profit by Sentiment

<img width="692" height="531" alt="pnl_by_sentiment" src="https://github.com/user-attachments/assets/852611be-3295-4d6e-ab00-f46ef947876b" />


🔍 Compares average trader profitability during different sentiment conditions.

---

## 📈 Trading Volume Analysis

<img width="677" height="531" alt="trading_volume" src="https://github.com/user-attachments/assets/0e6d67db-7d9c-4d72-af26-9a4e16e24aa6" />


🔍 Highlights how market sentiment impacts trading activity and participation.

---

## 🔄 Buy vs Sell Activity

<img width="777" height="531" alt="buy_vs_sell" src="https://github.com/user-attachments/assets/9ff242ca-6a42-48e3-a7cb-1ca09b8e1baf" />


🔍 Compares Buy and Sell behavior during Fear and Greed market conditions.

---

## 🏆 Top 10 Most Profitable Traders

<img width="843" height="769" alt="top_traders" src="https://github.com/user-attachments/assets/5889e7d8-437b-4361-a58c-aba99935db41" />


🔍 Identifies traders with the highest cumulative profitability.

---

## 📊 Win Rate by Market Sentiment

<img width="684" height="531" alt="win_rate_sentiment" src="https://github.com/user-attachments/assets/bbc34cae-db27-449e-ab58-e40f5e2366e8" />


🔍 Displays trader win percentages across different sentiment conditions.

---

## ⚠️ Profit Volatility Analysis

<img width="700" height="531" alt="profit_voltality_sentiment" src="https://github.com/user-attachments/assets/be15ff35-3191-4f91-b1c5-c63dbdd7f9e8" />

🔍 Shows how profit volatility changes during Fear and Greed market phases.

---

## 📉 PnL Distribution Analysis

<img width="878" height="531" alt="pnl_dist_sentimet" src="https://github.com/user-attachments/assets/6a968094-b572-4123-9a0f-41317134b15c" />


🔍 Visualizes the spread and consistency of trader profitability.

---

## 📅 Daily Profit Trend

![Daily Profit Trend](images/daily_profit_trend.png)

🔍 Displays daily fluctuations in overall trader profitability.

---

## 🔥 Correlation Heatmap

<img width="837" height="526" alt="corelation_heatmap" src="https://github.com/user-attachments/assets/fde6a686-a89b-4244-bc99-6adf3bca5caf" />




🔍 Displays relationships between important trading metrics such as:
- Execution Price
- Trade Size
- Closed PnL
- Fees
- Sentiment Value



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
    ├── win_rate.png
    ├── volatility.png
    ├── pnl_distribution.png
    ├── daily_profit_trend.png
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
| 📉 Stability | Fear periods resulted in inconsistent profitability patterns |
| 📅 Market Trends | Daily profit trends fluctuated significantly during volatile phases |

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

To keep the repository lightweight and easier to review, the original dataset links are provided in the Dataset File

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
