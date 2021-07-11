import requests
from bs4 import BeautifulSoup


class SongGenerator:
    
    # Initializing information for web scraping.
    def __init__(self):
        self.playlist_date = input("Hello! This program will create a Spotify playlist from a specific date for you.\n"
                                   "What date would you like the songs to be from? Enter in YYYY-mm-dd format.")
        self.billboard_URL = "https://www.billboard.com/charts/hot-100/" + self.playlist_date
    
    # Obtaining song titles by scraping website.
    def get_songs(self):
        response = requests.get(self.billboard_URL)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            song_name_spans = soup.find_all(name="span",
                                            class_="chart-element__information__song text--truncate color--primary")
            song_names = []
            for song_name_span in song_name_spans:
                song_names.append(song_name_span.getText())
            return song_names
        else:
            self.playlist_date = input("Incorrect date format, please enter again.")
            self.billboard_URL = "https://www.billboard.com/charts/hot-100/" + self.playlist_date
            song_names = self.get_songs()
            return song_names
