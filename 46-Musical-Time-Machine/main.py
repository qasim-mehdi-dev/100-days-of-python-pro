
import os
import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic

if not os.path.exists("browser.json"):
    print("Authentication file missing. Please run auth_setup.py first.")
    exit()

date = input("Which year/date do you want to travel to? (e.g., 2014-04-19): ").strip()

url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"
print(f"Accessing Bakeboard mirror for {date}...")

response = requests.get(url)

if response.status_code != 200:
    print(f"Could not find a chart page for date: {date}.")
    exit()

soup = BeautifulSoup(response.text, "html.parser")
song_names = [tag.getText().strip() for tag in soup.select("h3.chart-entry__title")]
print(f"Successfully extracted {len(song_names)} tracks.")

print("\nLogging into YouTube Music session...")
yt = YTMusic("browser.json")

playlist_name = f"{date} Billboard 100"
print("Generating remote playlist container...")
playlist_id = yt.create_playlist(
    title=playlist_name,
    description=f"Top songs from {date} compiled via automated Python parser.",
    privacy_status="PRIVATE",
)
print(f"Created remote playlist container: {playlist_name}")

print("\nExecuting remote sync engine...")
for rank, song in enumerate(song_names, start=1):
    search_results = yt.search(song, filter="songs", limit=1)
    if search_results:
        video_id = search_results[0]["videoId"]
        yt.add_playlist_items(playlist_id, [video_id])
        print(f"[{rank}/100] Added: {song}")
    else:
        print(f"[{rank}/100] Skipped (No database match): {song}")

print("\nPIPELINE RUN COMPLETE! Check your YouTube Music App library!")