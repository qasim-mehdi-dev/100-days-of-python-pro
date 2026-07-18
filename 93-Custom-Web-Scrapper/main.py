import requests
from bs4 import BeautifulSoup
import csv

TARGET_URL = "https://news.ycombinator.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

def fetch_page_data(url, headers):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.text
    except requests.RequestException as error:
        print(f"Error Fetching Page Data: {error}")
        return None
    
def extract_scrapped_items(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    scrapped_data = []

    containers = soup.find_all("tr", class_="athing")

    for container in containers:
        try:
            rank = container.find("span", class_="rank").text.strip().replace(".", "")
            
            title_box = container.find("span", class_="titleline")
            anchor = title_box.find("a")
            
            title = anchor.text.strip()
            link = anchor["href"]

            item = {
                "rank": rank,
                "title": title,
                "link": link,
            }
            scrapped_data.append(item)
        except (AttributeError, TypeError):
            continue

    return scrapped_data
def save_data_to_csv(data_list, filename):
    if not data_list:
        print("no Data found to save")
        return
    
    fieldnames = data_list[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_list)

    print(f"Data Successfully saved to: {filename}.")

if __name__ == "__main__":
    url = TARGET_URL
    headers = HEADERS

    raw_html = fetch_page_data(url, headers)

    if raw_html is not None:
        parsed_results = extract_scrapped_items(raw_html)
        save_data_to_csv(parsed_results, 'scraped_output.csv')