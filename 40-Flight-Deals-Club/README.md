# Day 40: Flight Club Capstone Engine (Part 2)

A Python-based automated flight tracking engine that monitors destination pricing thresholds via APIs and broadcasts alerts to an email distribution club. This project expands on the Core Flight Engine by integrating customer club distribution channels.

## 🚀 Features

* **Live Destination Tracking:** Synchronizes with a Sheety API backend to pull target vacation destinations and their threshold prices.
* **Flight Search Infrastructure:** Queries the Amadeus API to scan for upcoming routes, flight frequencies, and return dates up to 6 months out.
* **Resilient Architecture:** Features an optimized local data fallback system to maintain stability and prevent script crashes during external API configuration errors.
* **Graceful Exception Handling:** Built-in `try-except` guardrails for `smtplib` communication blocks, ensuring a clean `exit code 0` sequence during runtime.

---

## 🛠️ Tech Stack & Concepts Used

* **Language:** Python 3.14
* **APIs Used:** Amadeus (Flight Tracking Engine), Sheety (Google Sheets Workspace Layer)
* **Core Libraries:** `requests`, `requests_cache`, `smtplib`, `dotenv`, `os`
* **Architecture Concepts:** Object-Oriented Programming (OOP), Data Normalization, List Comprehension, API Layer Abstraction.

---

## 📂 Project Structure

```text
40-Flight-Deals-Club/
│
├── 40-Flight-Deals-Club.py    # Main orchestration script
├── data_manager.py            # Sheety API interface & Local Data Backup Layer
├── flight_search.py           # Amadeus API connection engine
├── flight_data.py             # Data structure logic for parsing flight paths
├── notification_manager.py    # Email notification router (with SMTP fail-safes)
├── .env                       # Local environment secrets storage (Git ignored)
└── README.md                  # Project documentation