import requests
from bs4 import BeautifulSoup

date = input("What year would you like to travel to? ( YYYY/MM/DD ): ").split("/")
year, month, day = [str(i) for i in date]
url = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"
song_name = []
song_number = []
song_artist = []

webpage = requests.get(url).text
soup = BeautifulSoup(webpage, "html.parser")
song_list = soup.find_all("div", class_="o-chart-results-list-row-container")
for i in song_list:
    song_name.append(i.findNext("h3", class_="c-title").text.strip())
    song_number.append(i.findAllNext("span", class_="c-label")[0].text.strip())
    song_artist.append(i.findAllNext("span", class_="c-label")[1].text.strip())

top100 = []
for i in range(100):
    top100.append(f"{song_number[i]} - {song_name[i]}: {song_artist[i]}")
print(top100)