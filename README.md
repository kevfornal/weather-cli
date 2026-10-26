# Weather & Air Quality CLI (`weather-cli`)

A lightweight Python command-line interface tool designed to fetch current weather data and atmospheric metrics for any specified global city using external API endpoints.

## 📌 Features

*   **City-Based Weather Lookup:** Retrieve current atmospheric conditions by providing a target city name via command-line arguments.
*   **Error & Input Handling:** Validates user inputs to ensure prompt user guidance when command-line parameters are missing.
*   **Clean Output Formatting:** Terminal-optimized formatting for clear data presentation.
*   **Production-Ready Git Standards:** Includes standard Python `.gitignore` patterns and dependency manifests for easy collaboration.

---

## 🛠️ Project Structure

```text
weather-cli/
├── weather.py         # Main executable script for CLI operations
├── requirements.txt   # Core project dependencies (requests)
├── .gitignore         # Python-specific build/environment exclusions
└── README.md          # Project documentation
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites

Ensure you have **Python 3.8+** installed on your system.

### 2. Installation & Setup

Clone the repository and set up your environment:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/weather-cli.git
cd weather-cli

# Optional: Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 💻 Usage

Run the `weather.py` script by providing the city name as a command-line argument:

```bash
# Fetch weather for London
python weather.py "London"

# Fetch weather for New York
python weather.py "New York"
```

### Example Execution & Output

```text
$ python weather.py "London"
Fetching weather for: London...
```

*If no city argument is provided, the script outputs guidance:*

```text
$ python weather.py
Please provide a city name. Example: python weather.py 'London'
```

---

## ⚙️ Configuration & API Setup

1. Open `weather.py` to add custom API keys (e.g., from OpenWeatherMap).
2. Integrate additional metrics such as humidity, wind speed, or Air Quality Index (AQI) as required.
