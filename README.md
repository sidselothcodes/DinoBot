
# DinoBot – Google Dinosaur Game Automation Bot

Welcome to **DinoBot**, a Python-based automation project that plays the Google Dinosaur game autonomously. Using **Selenium WebDriver** and **PyAutoGUI**, this bot detects obstacles in real-time with pixel-based recognition and simulates key presses to help the dinosaur jump over obstacles.

---

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [How It Works](#how-it-works)
- [Usage](#usage)

---

## Features
- Automates the **Google Chrome Dinosaur Game** using **Python**.
- Uses **PyAutoGUI** for pixel-based obstacle detection.
- Simulates real-time key presses to control the dinosaur’s movements.
- Dynamic obstacle handling as game speed increases.
- Uses **Selenium WebDriver** to automate browser interactions.
- Supports **incognito mode** to avoid ad interference.

---

## Technologies Used
- **Python** – Core programming language used.
- **Selenium WebDriver** – Automates browser interactions.
- **PyAutoGUI** – Simulates key presses and mouse movements.
- **PyGetWindow** – Manages browser window focus and activation.
- **ChromeDriver** – Controls Chrome browser automation.
- **macOS Environment** – Tested on macOS.

---

## Setup and Installation

### 1. Prerequisites
- **Python 3.x** installed. You can verify with:

    ```bash
    python3 --version
    ```

- **Google Chrome** installed and updated to the latest version.
- **ChromeDriver** installed. Make sure the version matches your installed Chrome version. Download it from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).

### 2. Clone the Repository
```bash
git clone https://github.com/sidselothcodes/DinoBot.git
cd DinoBot
```

### 3. Install Required Python Packages
```bash
pip install selenium pyautogui pillow pygetwindow
```

### 4. Set Up ChromeDriver
- Place the `chromedriver` binary in `/usr/local/bin/` or specify its path in the code.

---

## How It Works

1. **Selenium** opens the Chrome browser and navigates to the **Dinosaur Game**.
2. The bot **maximizes the browser window** to ensure the correct coordinates.
3. **PyAutoGUI** captures screenshots and detects obstacles based on **pixel values**.
4. When an obstacle is detected, the bot **presses the spacebar** to make the dinosaur jump.
5. The bot dynamically **adjusts detection points** as the game speed increases.

---

## Usage

1. **Run the Script:**  
   Make sure you are in the project directory and run:

   ```bash
   python3 dinosaur_game_bot.py
   ```

2. **Expected Behavior:**
   - The bot will open **Google Chrome** and start the game.
   - The dinosaur will **jump over obstacles automatically**.
   - The game will adjust detection points as speed increases.

3. **Debugging Pixel Values (Optional):**  
   If you encounter issues with obstacle detection, uncomment the following lines in the script:

   ```python
   print(f"Pixel 1: {im.getpixel((XCOR_1, YCOR))}")
   print(f"Pixel 2: {im.getpixel((XCOR_2, YCOR))}")
   print(f"Pixel 3: {im.getpixel((XCOR_1 + 1, YCOR))}")
   ```

---
