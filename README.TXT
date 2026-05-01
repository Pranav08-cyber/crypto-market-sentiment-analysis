# Bitcoin Market Sentiment vs Trader Performance Analysis

## Objective

The objective of this project is to analyze the relationship between Bitcoin market sentiment and trader performance using Hyperliquid historical trading data and the Fear & Greed Index.

This analysis explores how market psychology impacts:

- Trader profitability
- Trading volume
- Risk-taking behavior
- Buy/Sell activity
- Market participation
- Overall trading performance

The project aims to uncover meaningful insights that can help build smarter trading strategies and improve decision-making during different market conditions.

---

# Datasets Used

## 1. Bitcoin Fear & Greed Index Dataset

This dataset contains daily market sentiment classifications such as:

- Fear
- Extreme Fear
- Greed
- Extreme Greed

Columns used:
- Date
- Classification
- Sentiment Value

---

## 2. Hyperliquid Historical Trader Dataset

This dataset contains historical trading activity information including:

- Account
- Symbol
- Execution Price
- Trade Size
- Side (Buy/Sell)
- Closed PnL
- Leverage
- Timestamp
- Trading Fees

---

# Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

# Project Workflow

The following steps were performed during the analysis:

1. Data loading
2. Data cleaning
3. Date formatting
4. Dataset merging
5. Exploratory Data Analysis
6. Sentiment-based trader analysis
7. Profitability analysis
8. Volatility analysis
9. Visualization and insight generation

---

# Data Cleaning

The following preprocessing steps were performed:

- Removed duplicate records
- Converted timestamp columns into datetime format
- Created a common date column for merging
- Converted important columns into numeric format
- Merged both datasets using trade dates

---

# Exploratory Data Analysis

The analysis focused on identifying patterns between market sentiment and trader behavior using multiple visualizations and statistical summaries.

The following analyses were performed:

- Market sentiment distribution
- Average profit by sentiment
- Trading volume analysis
- Buy vs Sell behavior
- Top profitable traders
- Win rate analysis
- Volatility analysis
- Correlation analysis
- Daily PnL trends

---

# Visualizations

## 1. Market Sentiment Distribution

![Market Sentiment Distribution](images/sentiment_distribution.png)

This chart shows the distribution of different market sentiment categories across the dataset.

---

## 2. Average Trader Profit by Sentiment

![Average Trader Profit](images/pnl_by_sentiment.png)

This visualization compares average trader profitability during different sentiment conditions.

---

## 3. Trading Volume Analysis

![Trading Volume](images/trading_volume.png)

This chart highlights how trading activity changes across Fear and Greed market conditions.

---

## 4. Buy vs Sell Activity

![Buy Sell Analysis](images/buy_sell_analysis.png)

This visualization compares buy and sell behavior under different market sentiment conditions.

---

## 5. Top 10 Most Profitable Traders

![Top Traders](images/top_traders.png)

This chart identifies the most profitable traders based on total closed PnL.

---

## 6. Correlation Heatmap

![Correlation Heatmap](images/correlation_heatmap.png)

This heatmap shows relationships between key trading variables such as:

- Execution Price
- Trade Size
- Closed PnL
- Fees
- Sentiment Value

---

# Key Insights

- Market sentiment has a strong influence on trader behavior and profitability.

- Greed periods generally showed higher average profits and stronger market participation.

- Fear periods were associated with higher volatility and inconsistent trader performance.

- Trading volume increased significantly during bullish market sentiment conditions.

- Buy activity was generally stronger during Greed periods, while Fear periods triggered more defensive trading behavior.

- A small number of traders contributed a large portion of overall profitability.

- Some traders remained consistently profitable regardless of sentiment conditions, indicating disciplined trading strategies.

- Profit volatility increased during uncertain market conditions.

- Market psychology directly affected trader confidence and risk appetite.

- Sentiment indicators such as the Fear & Greed Index can provide valuable signals for improving trading decisions.

- Combining market sentiment with trader performance data can help optimize strategy selection and risk management.

- Sentiment-based analysis can help identify high-risk and high-opportunity trading periods.

---

# Conclusion

This project explored the relationship between Bitcoin market sentiment and trader performance using Hyperliquid trading data and the Fear & Greed Index.

The analysis demonstrated that market sentiment significantly impacts:

- Trading activity
- Trader profitability
- Market participation
- Risk-taking behavior
- Profit volatility

The findings suggest that sentiment indicators can be useful tools for improving trading strategies, optimizing decision-making, and managing risk under different market conditions.

---

# How to Run the Project

Install required libraries:

```bash
pip install pandas matplotlib seaborn
```

Run the analysis script:

```bash
python analysis.py
```

---

# Project Files

```text
crypto-sentiment-analysis/
│
├── analysis.py
├── historical_data.xlsx.csv
├── fear_greed_index.xlsx.csv
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

# Final Outcome

This project successfully analyzed how Bitcoin market sentiment influences trader performance and market behavior.

The analysis provides meaningful insights that can help traders:

- Improve strategy selection
- Optimize trade timing
- Manage risks more effectively
- Understand market psychology better
- Make smarter trading decisions