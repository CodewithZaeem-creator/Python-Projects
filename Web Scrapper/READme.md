# 📰 News Headline Scraper

A Python web scraper that fetches the latest tech news headlines from Hacker News and saves them to a text file with a timestamp — fully automated, one run and you have today's news saved locally.

> My sixth Python project — learning web scraping, HTML parsing, and saving data to files. 🐍

---

## 🎮 Demo

```
================================
     📰 News Headline Scraper
================================

🔍 Fetching headlines from https://news.ycombinator.com...

📰 Found 30 headlines:

1. Python 4.0 announced with major new features
   🔗 https://python.org/news/...

2. GitHub launches new AI coding tool
   🔗 https://github.com/...

✅ Headlines saved to headlines_2025-01-01_14-30.txt!
```

---

## ✨ Features

- 🌐 Scrapes live headlines from [Hacker News](https://news.ycombinator.com) in real time
- 🔗 Saves both the headline title and the full link
- 💾 Saves to a `.txt` file with date and time in the filename
- 📂 Automatically opens the saved file after scraping
- ⚠️ Handles errors — checks if the website is reachable before scraping
- 🕐 Every file has a unique timestamp so nothing gets overwritten

---

## 🚀 Getting Started

### 1. Make sure Python is installed

```bash
python --version
```

Download from [python.org](https://www.python.org/downloads/) if needed.

### 2. Clone the repository

```bash
git clone https://github.com/CodewithZaeem-creator/Python-Projects.git
cd Python-Projects/news-scraper
```

### 3. Install the required libraries

```bash
pip install requests beautifulsoup4
```

### 4. Run the scraper

```bash
python web_scrapper.py
```

The headlines will print on screen and a `.txt` file will open automatically. ✅

---

## 📦 Requirements

| Requirement | Notes |
|---|---|
| Python 3.9+ | Download from [python.org](https://www.python.org) |
| `requests` | Install via pip — fetches the webpage |
| `beautifulsoup4` | Install via pip — reads the HTML |
| `datetime` | Built-in — nothing to install |
| `os` | Built-in — nothing to install |

---

## 🧠 How It Works

```
requests.get() fetches the Hacker News webpage
              ↓
BeautifulSoup reads through all the HTML
              ↓
find_all() locates every headline span
              ↓
Loop collects each title and link
              ↓
Prints everything on screen
              ↓
Saves to headlines_YYYY-MM-DD_HH-MM.txt
              ↓
os.startfile() opens the file automatically 📂
```

---

## 📄 Output File Format

```
📰 News Headlines
Scraped from: https://news.ycombinator.com
Date: 2025-01-01 14:30
==================================================

1. Python 4.0 announced with major new features
   Link: https://python.org/news/...

2. GitHub launches new AI coding tool
   Link: https://github.com/...
```

---

## 🌐 How to Scrape Other Websites

This is the most useful thing to learn about web scraping. Here is the exact process for scraping **any** website:

### Step 1 — Find the HTML element

1. Go to the website in Chrome or Edge
2. Right click on the text you want to scrape
3. Click **Inspect**
4. Look at the highlighted HTML — find the tag and class name

For example if you see this in the HTML:
```html
<h2 class="article-title">Breaking News Today</h2>
```

You write:
```python
soup.find_all("h2", class_="article-title")
```

### Step 2 — Change the URL and selector

Just swap out two things in the code:

```python
# change this to any website
url = "https://any-website.com"

# change this to match the tag and class you found
headlines = soup.find_all("tag", class_="classname")
```

### Step 3 — Practice website examples

These websites are built for scraping practice — no blocks, no restrictions:

**Quotes:**
```python
url = "https://quotes.toscrape.com"
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
```

**Book titles and prices:**
```python
url = "https://books.toscrape.com"
titles = soup.find_all("h3")
prices = soup.find_all("p", class_="price_color")
```

**Hacker News headlines (this project):**
```python
url = "https://news.ycombinator.com"
headlines = soup.find_all("span", class_="titleline")
```

### Step 4 — The universal scraping template

Use this as your starting point for any website:

```python
import requests
from bs4 import BeautifulSoup

url = "https://website-you-want.com"
response = requests.get(url)

if response.status_code != 200:
    print("Could not reach website")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# change "tag" and "classname" to what you found in Inspect
items = soup.find_all("tag", class_="classname")

for item in items:
    print(item.get_text())
```

That template works for almost any website — just change the URL and the selector. 🎯

---

## 📁 Project Structure

```
news-scraper/
│
├── web_scrapper.py           # All the scraper logic
├── headlines_2025-01-01.txt  # Example output file (auto-generated)
└── README.md                 # This file
```

---

## 💡 Ideas for What to Add Next

- 🔁 **Scrape multiple pages** — Hacker News has page 2, 3, 4... scrape them all
- 📊 **Save to CSV** — open in Excel and filter/sort the headlines
- 🔍 **Keyword filter** — only save headlines containing words like "Python" or "AI"
- ⏰ **Schedule it** — run automatically every morning using Windows Task Scheduler
- 📧 **Email the results** — send yourself the headlines using Python's `smtplib`

---

## 🌱 What I Learned

- How web scraping works — fetching and parsing real HTML from the internet
- How to use `requests` to download a webpage in Python
- How `BeautifulSoup` finds specific elements inside HTML
- How right click → Inspect reveals the HTML structure of any website
- How `datetime` creates timestamps for unique filenames
- How to write data to a `.txt` file with proper formatting
- How `status_code` checks if a website request succeeded or failed

---

## ⚠️ Disclaimer

This scraper is built for educational purposes. Always check a website's `robots.txt` and terms of service before scraping. Hacker News allows scraping for personal and educational use.

---

## 📄 License

MIT License — free to use, modify, and share.

---

*Made with ❤️ as part of my Python learning journey. If you found this useful, leave a ⭐ on GitHub!*
