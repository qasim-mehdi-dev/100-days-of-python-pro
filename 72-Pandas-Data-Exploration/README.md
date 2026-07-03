# Day 72: High-Paying Careers Data Exploration 📊

An analytical deep-dive into college major salary data using the **Pandas** library. This project focuses on importing, inspecting, and sanitizing raw data configurations to extract actionable insights on long-term career risk versus potential reward.

## 🛠️ Concepts & Methods Mastered

### 1. Data Cleaning & Sanitization
* `df.isna()`: Scanned the entire dataset to uncover missing or corrupted elements.
* `df.dropna()`: Stripped out broken footer elements and incomplete records to maintain math integrity.

### 2. Analytical Target Retrieval
* **Bracket Notation** (`df['Column']`): Target and isolate unique columns for numerical evaluation.
* `.idxmax()`: Discovered structural row indexes housing the absolute peak metrics in specific data series.
* `.loc[]`: Performed label-based lookup to extract whole-row data records via specific indexes.

### 3. Financial Risk Analysis
* **Series Engineering**: Subtracted the 10th percentile salary values from the 90th percentile to establish an custom career 'Spread'.
* `.sort_values()`: Filtered data ascending (lowest risk) and descending (highest upside potential) to benchmark fields.

### 4. High-Level Aggregation
* `.groupby()`: Unified 50 diverse majors into generalized field categories (`STEM`, `Business`, `HASS`).
* `.mean(numeric_only=True)`: Leveraged updated Pandas core workflows to cleanly bypass text records when pulling industry averages.

### 5. Formatting Configuration
* `pd.options.display.float_format`: Reconfigured global display layouts to shift messy float points into clean, comma-separated currency visuals.

## 📈 Key Discovery
* **Highest Starting Salary:** Physician Assistant ($74,300.00)
* **Highest Volatility/Potential:** Economics (Largest earning gap)
* **Lowest Risk/Most Stable:** Nursing (Tighter salary bracket floor)
* **Industry Overview:** `STEM` fields systematically sweep the upper tier of starting, mid-career, and high-percentile brackets.