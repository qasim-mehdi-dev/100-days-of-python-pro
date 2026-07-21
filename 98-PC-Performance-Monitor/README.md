# Smart PC Hardware & Performance Monitor Widget

A real-time, desktop telemetry widget built with Python using `psutil` and `Tkinter`. It provides live tracking of core system metrics including CPU load, RAM allocation, and storage utilization with dynamic visual threshold warnings.

## ⚡ Features
* **Live System Telemetry:** Real-time polling of CPU utilization, RAM usage, and primary disk statistics.
* **Hardware Detection:** Automatically queries physical CPU core counts and logical execution threads.
* **Dynamic Warning System:** Changes text color indicators when system resources breach heavy utilization thresholds (> 85%).
* **Lightweight Dark-Mode UI:** Minimalist overlay styled with standard GUI components designed for zero background overhead.

## 🛠️ Stack & Libraries
* **Python 3**
* **`psutil`** (Cross-platform process and system monitoring)
* **`tkinter` / `ttk`** (Native Python GUI toolkit)

## 📁 Repository Structure
```text
.
├── main.py        # Core application GUI & polling event loop
└── README.md      # Technical documentation