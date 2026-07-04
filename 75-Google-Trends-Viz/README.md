# Google Trends & Data Visualisation

A data analysis project using Pandas and Matplotlib to analyze how public Google Search volume correlates with real-world financial assets and macroeconomic shifts. 

## 🚀 Project Overview
This project processes, aligns, and visualizes time-series data from distinct sources (Google Trends, historical stock prices, asset valuations, and federal unemployment records). It explores whether public web interest behaves as a leading, lagging, or parallel indicator for market breakouts and economic turning points.

## 🛠️ Concepts & Methods Learned
* **Time-Series Alignment & Resampling:** Used `.resample('ME')` to compress high-frequency daily asset data into monthly buckets, matching the frequency of Google Trends data.
* **Dual-Axis Charting:** Implemented `.twinx()` to cleanly overlay two independent datasets (e.g., search volume index vs. USD asset price) over a shared timeline.
* **Advanced Date Locators:** Configured `mdates.YearLocator()` and `mdates.DateFormatter('%Y')` to format cluttered timestamps into clean, readable annual grid tick marks.
* **Data Smoothing (Rolling Averages):** Applied a 6-month moving average using `.rolling(window=6).mean()` to strip out annual seasonal noise from unemployment data and isolate macro trajectories.
* **Chart Polishing:** Customized plot boundaries (`.set_xlim()`, `.set_ylim()`), line weights, marker styles (`marker='o'`), line configurations (`linestyle='--'`), and text rotation to create production-ready charts.

## 📊 Core Data Insights
1. **Tesla:** Web search volume surges closely mirrored or slightly preceded massive price breakouts in stock valuation.
2. **Bitcoin:** Public search volume heavily coupled with price spikes during massive hype cycles (like late 2017) but decoupled significantly during later market cycles.
3. **Unemployment:** Google search traffic for job benefits acts as a powerful leading economic indicator, shifting upward weeks before official federal government statistics capture the actual rise in unemployment rates.

## 💻 Tech Stack
* Python 3
* Pandas
* Matplotlib