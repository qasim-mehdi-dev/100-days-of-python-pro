# Custom Web Scraper (Hacker News)

A robust, lightweight web scraping utility built with Python to parse and extract data from live web structures. This project avoids basic bot detection using custom header injections, navigates deeply nested HTML tables, and exports the parsed live data into structured files.

## 🚀 Features
* **Live DOM Parsing:** Targets Hacker News structural layout hooks (`tr.athing`, `span.titleline`) to pull dynamic content.
* **Resilient Architecture:** Implements connection error handling using `requests.RequestException` and protects elements inside iteration loops against missing fields using selective `AttributeError`/`TypeError` exceptions.
* **Persistent Storage:** Synchronously maps structured dictionaries into standard comma-separated datasets (`.csv`) with automatic header generation.
* **Anti-Bot Simulation:** Integrates custom request headers (`User-Agent`, `Accept-Language`) to simulate human browser traffic patterns safely.

## 🛠️ Built With
* Python 3
* Requests (HTTP Client Library)
* Beautiful Soup 4 (HTML Parser)
* CSV (Built-in Data Serialization Module)

## 📁 Repository Structure
```text
.
├── main.py            # Core scraping engine and extraction loops
├── scraped_output.csv # Extracted data file (Rank, Title, URL)
└── README.md          # Project documentation