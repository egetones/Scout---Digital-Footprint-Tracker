# Scout - Digital Footprint Tracker

**Scout** is a lightweight, Python-based Open Source Intelligence (OSINT) tool designed to check the availability of a specific username across popular social media platforms and websites. 

Unlike simple status code checkers, Scout includes a **"Smart Detection"** mechanism to eliminate false positives by analyzing page content, ensuring higher accuracy.

## Features

* **Multi-Platform Support:** Checks Instagram, Twitter/X, GitHub, Facebook, Twitch, Steam, and more.
* **Smart Detection:** Analyzes HTML content to distinguish between actual profiles and "soft 404" or redirection pages (prevents false positives).
* **User-Agent Rotation:** Uses realistic headers to mimic browser activity.
* **Colorized Output:** Clean and easy-to-read terminal interface using `colorama`.
* **Fast & Lightweight:** Built with `requests` for quick enumeration.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/scout-tracker.git](https://github.com/yourusername/scout-tracker.git)
    cd scout-tracker
    ```

2.  **Install dependencies:**
    You need Python 3 installed. Then run:
    ```bash
    pip install requests colorama
    ```

## Usage

Simply run the script using Python:

```bash
python scout.py
```

# Legal Disclaimer

For Educational Purposes Only. This tool is intended to help security researchers and red teamers understand digital footprints and reconnaissance techniques. The developer is not responsible for any misuse of this tool or any illegal activities performed with it. Always obtain proper authorization before investigating targets.
