import requests
from bs4 import BeautifulSoup
import csv
import time
import os
import sys

def clean_number(text):
    return ''.join(c for c in text if c.isdigit())

def get_country_page(country):
    filename = f"cache/{country}.html"

    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()

    try:
        url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        html = response.text

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)

        time.sleep(1)
        return html

    except Exception as e:
        print(f"Ошибка загрузки {country}: {e}")
        return None

def extract_data(html, country):
    soup = BeautifulSoup(html, "html.parser")
    capital = area = population = ""

    table = soup.find("table", class_="infobox")
    if not table:
        return capital, area, population

    for row in table.find_all("tr"):
        th = row.find("th")
        td = row.find("td")

        if not th or not td:
            continue

        label = th.get_text().lower()
        value = td.get_text()

        if "capital" in label and not capital:
            capital = ""
            for char in value:
                if char.isdigit() or char == '[':
                    break
                capital += char
            capital = capital.strip()

        if not area:
            if "area" in label or "total" in label:
                if "km" in value.lower():
                    area = clean_number(value)
            elif "area" in label:
                area = clean_number(value)

        if not population:
            if "population" in label:
                population = clean_number(value)
            elif "estimate" in label and any(c.isdigit() for c in value):
                population = clean_number(value)
            elif "census" in label and not population:
                population = clean_number(value)

    return capital, area, population

if len(sys.argv) != 3:
    print("Использование: python script.py countries.txt countries_data.csv")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists("cache"):
    os.makedirs("cache")

with open(input_file, "r", encoding="utf-8") as f:
    countries = [line.strip() for line in f if line.strip()]

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["country", "city", "area", "population"])

    for country in countries:
        print(f"Обрабатываю: {country}")

        html = get_country_page(country)
        if html:
            city, area, population = extract_data(html, country)
            writer.writerow([country, city, area, population])
        else:
            writer.writerow([country, "", "", ""])