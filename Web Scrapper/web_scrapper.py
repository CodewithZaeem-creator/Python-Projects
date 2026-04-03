
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

print("================================")
print("     📰 News Headline Scraper   ")
print("================================")

# the website we are scraping
url = "https://news.ycombinator.com"

print(f"\n🔍 Fetching headlines from {url}...")

# Step 1 - fetch the webpage
response = requests.get(url)

# check if it worked
if response.status_code != 200:
    print("❌ Could not reach the website. Check your internet connection.")
    exit()

# Step 2 - read the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3 - find all headlines
headlines = soup.find_all("span", class_="titleline")

if not headlines:
    print("❌ No headlines found.")
    exit()

# Step 4 - print and collect them
print(f"\n📰 Found {len(headlines)} headlines:\n")

all_headlines = []

for index, headline in enumerate(headlines, start=1):
    # get the text
    title = headline.get_text()

    # get the link if there is one
    link_tag = headline.find("a")
    link = link_tag["href"] if link_tag else "No link"

    print(f"{index}. {title}")
    print(f"   🔗 {link}\n")

    all_headlines.append(f"{index}. {title}\n   Link: {link}")

# Step 5 - save to a file
# create a filename with today's date and time
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
filename = f"headlines_{timestamp}.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write("📰 News Headlines\n")
    file.write(f"Scraped from: {url}\n")
    file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    file.write("=" * 50 + "\n\n")

    for headline in all_headlines:
        file.write(headline + "\n\n")

print(f"✅ Headlines saved to {filename}!")

# open the file automatically
os.startfile(filename)