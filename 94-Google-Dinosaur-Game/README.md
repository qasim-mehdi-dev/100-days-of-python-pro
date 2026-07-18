# Google Dinosaur Game Automation Bot

A fun automation script written in Python that utilizes real-time screen parsing (computer vision concepts) and programmatic peripheral inputs to autonomously play Google Chrome's hidden dinosaur game (`chrome://dino/`).

## 🚀 How It Works
* **Perceptual Bounding Box:** Continuously captures a micro-snapshot (`ImageGrab`) of a specific geometric bounding box positioned directly in front of the dinosaur's path.
* **Grayscale Pixel Analysis:** Converts the captured color space to 8-bit grayscale pixels (`L` mode) to perform low-overhead luminosity calculations.
* **Dynamic Input Triggering:** Simulates a system-level hardware keyboard stroke (`pyautogui.press`) the millisecond a contrast delta matches an approaching obstacle.
* **Fail-Safe Protection:** Implements PyAutoGUI's hardware fail-safe threshold, allowing instant execution termination by moving the cursor to the coordinate origin `(0,0)`.

## 🛠️ Requirements
* Python 3
* PyAutoGUI (GUI Automation)
* Pillow (Image Processing)

## 📁 Repository Structure
```text
.
├── main.py        # Main execution loop and pixel analysis engine
├── dino_test.png  # Debugging asset showing active detection field boundary
└── README.md      # Project documentation