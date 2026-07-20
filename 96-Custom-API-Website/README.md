# Crypto Asset Search Engine (CoinGecko REST API)

A clean Flask backend web application that interfaces with the CoinGecko REST API v3 to search, filter, and parse live cryptocurrency market data asynchronously.

## 🚀 Key Technical Features
* **Modular Service Architecture:** Decouples HTTP networking logic (`requests`) from Flask controller routes.
* **Environment Configuration:** Uses `python-dotenv` for key management and local environment isolation.
* **Data Sanitization Layer:** Filters external API responses down to lean data transfer structures before client delivery.
* **Dual Request Handling:** Supports both traditional form submissions (`POST`) and RESTful URI query strings (`GET`).

## 🛠️ Stack
* Python 3
* Flask (Web Framework)
* Requests (HTTP Engine)
* CoinGecko API v3 (Market Data)

## 📁 Repository Structure
```text
.
├── templates/
│   └── index.html     # Search interface
├── .env               # Private API keys (Git ignored)
├── .gitignore         # Security exclusions
├── main.py            # Flask routes and REST orchestration
└── README.md          # Project documentation