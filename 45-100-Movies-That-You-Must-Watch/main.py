import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(URL, headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h2")

for movie in all_movies:
    print(movie.getText())

with open("movies.txt", "w") as file:
    for movie in all_movies[::-1]:
        file.write(f"{movie.getText()}\n")
    print("Successfully written 100 movies to movies.txt! 🎬🍿")