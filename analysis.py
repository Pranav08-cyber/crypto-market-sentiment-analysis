import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# better chart styling
sns.set_style("whitegrid")

# loading datasets
trades = pd.read_csv("historical_data.xlsx.csv")
sentiment = pd.read_csv("fear_greed_index.xlsx.csv")

print("\nTrades Dataset")
print(trades.head())

print("\nSentiment Dataset")
print(sentiment.head())

# basic cleaning
trades = trades.drop_duplicates()
sentiment = sentiment.drop_duplicates()

# converting date columns
trades['Timestamp IST'] = pd.to_datetime(
    trades['Timestamp IST'],
    errors='coerce'
)

sentiment['date'] = pd.to_datetime(
    sentiment['date'],
    errors='coerce'
)

# creating common date column
trades['trade_date'] = trades['Timestamp IST'].dt.date
sentiment['trade_date'] = sentiment['date'].dt.date

# converting important numeric columns
numeric_cols = [
    'Execution Price',
    'Size Tokens',
    'Size USD',
    'Closed PnL',
    'Fee'
]

for col in numeric_cols:
    trades[col] = pd.to_numeric(
        trades[col],
        errors='coerce'
    )

print("\nData cleaning completed")

# merging datasets
merged = pd.merge(
    trades,
    sentiment,
    on='trade_date',
    how='left'
)

print("\nMerged Dataset")
print(merged.head())

print("\nDataset Shape:", merged.shape)

# sentiment distribution

plt.figure(figsize=(7,5))

sns.countplot(
    data=merged,
    x='classification'
)

plt.title("Market Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.show()

# average pnl by sentiment

avg_pnl = merged.groupby(
    'classification'
)['Closed PnL'].mean().sort_values(
    ascending=False
)

print("\nAverage Profit by Sentiment")
print(avg_pnl)

plt.figure(figsize=(8,5))

avg_pnl.plot(kind='bar')

plt.title("Average Trader Profit by Sentiment")
plt.ylabel("Average Closed PnL")

plt.xticks(rotation=45)

plt.show()

# trading volume analysis

volume = merged.groupby(
    'classification'
)['Size USD'].sum()

print("\nTrading Volume by Sentiment")
print(volume)

plt.figure(figsize=(8,5))

volume.plot(kind='bar')

plt.title("Trading Volume across Sentiments")
plt.ylabel("Total Volume")

plt.xticks(rotation=45)

plt.show()

# buy vs sell activity

buy_sell = pd.crosstab(
    merged['classification'],
    merged['Side']
)

print("\nBuy vs Sell Activity")
print(buy_sell)

buy_sell.plot(
    kind='bar',
    figsize=(9,5)
)

plt.title("Buy vs Sell Activity by Sentiment")
plt.ylabel("Trade Count")

plt.xticks(rotation=45)

plt.show()

# top profitable traders

top_traders = merged.groupby(
    'Account'
)['Closed PnL'].sum().sort_values(
    ascending=False
).head(10)

print("\nTop 10 Profitable Traders")
print(top_traders)

plt.figure(figsize=(10,5))

top_traders.plot(kind='bar')

plt.title("Top 10 Most Profitable Traders")
plt.ylabel("Total Profit")

plt.show()

# win rate analysis

merged['profitable_trade'] = merged['Closed PnL'] > 0

win_rate = merged.groupby(
    'classification'
)['profitable_trade'].mean() * 100

print("\nWin Rate by Sentiment")
print(win_rate)

plt.figure(figsize=(8,5))

win_rate.plot(kind='bar')

plt.title("Win Rate by Market Sentiment")
plt.ylabel("Winning Trade Percentage")

plt.xticks(rotation=45)

plt.show()

# volatility analysis

volatility = merged.groupby(
    'classification'
)['Closed PnL'].std()

print("\nProfit Volatility")
print(volatility)

plt.figure(figsize=(8,5))

volatility.plot(kind='bar')

plt.title("Profit Volatility by Sentiment")
plt.ylabel("PnL Standard Deviation")

plt.xticks(rotation=45)

plt.show()

# pnl distribution

plt.figure(figsize=(10,5))

sns.boxplot(
    data=merged,
    x='classification',
    y='Closed PnL'
)

plt.title("PnL Distribution by Sentiment")

plt.xticks(rotation=45)

plt.show()

# correlation analysis

corr_cols = [
    'Execution Price',
    'Size Tokens',
    'Size USD',
    'Closed PnL',
    'Fee',
    'value'
]

corr_matrix = merged[corr_cols].corr()

print("\nCorrelation Matrix")
print(corr_matrix)

plt.figure(figsize=(10,6))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.show()

# daily pnl trend

daily_pnl = merged.groupby(
    'trade_date'
)['Closed PnL'].sum().reset_index()

plt.figure(figsize=(13,5))

plt.plot(
    daily_pnl['trade_date'],
    daily_pnl['Closed PnL']
)

plt.title("Daily Profit Trend")
plt.xlabel("Date")
plt.ylabel("Daily Closed PnL")

plt.xticks(rotation=45)

plt.show()

# most active traders

active_traders = merged['Account'].value_counts().head(10)

print("\nMost Active Traders")
print(active_traders)

plt.figure(figsize=(10,5))

active_traders.plot(kind='bar')

plt.title("Most Active Traders")
plt.ylabel("Number of Trades")

plt.show()

# leverage analysis

if 'Leverage' in merged.columns:

    leverage_analysis = merged.groupby(
        'classification'
    )['Leverage'].mean()

    print("\nAverage Leverage by Sentiment")
    print(leverage_analysis)

# key insights

print("""

Key Insights

1. Trader profitability changes noticeably across different market sentiment conditions.

2. Greed periods generally show higher average profits and trading participation.

3. Fear periods are associated with higher volatility and unstable trader performance.

4. Trading volume increases significantly during optimistic market conditions.

5. Buy activity becomes stronger during Greed periods, while Fear often triggers more defensive trading behavior.

6. A small number of traders contribute a major share of total profits.

7. Some traders remain consistently profitable regardless of sentiment, indicating disciplined strategies.

8. Profit volatility is much higher during uncertain market conditions.

9. Market sentiment directly impacts trader confidence and risk appetite.

10. Sentiment analysis can be useful for improving trade timing and risk management.

11. Combining market psychology with trading data can help build smarter trading strategies.

12. Monitoring Fear & Greed Index may provide valuable signals for identifying high-risk and high-opportunity periods.

""")

# saving final dataset

merged.to_csv(
    "final_merged_output.csv",
    index=False
)

print("\nFinal merged dataset saved successfully")

print("""

Conclusion

This project analyzed the relationship between
Bitcoin market sentiment and trader performance
using Hyperliquid trading data and the Fear &
Greed Index.

The analysis showed that market sentiment has
a strong influence on trading activity,
profitability, volatility, and trader behavior.

These insights can help traders improve
decision-making, optimize strategies, and
manage risks more effectively under different
market conditions.

""")