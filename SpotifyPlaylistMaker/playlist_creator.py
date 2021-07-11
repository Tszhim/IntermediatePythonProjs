import spotipy
from spotipy.oauth2 import SpotifyOAuth


class PlaylistCreator:
    
    # Initialzing information necessary to use Spotipy API.
    def __init__(self):
        self.client_id = "your_client_id"
        self.client_secret = "your_client_secret"
        self.sp = self.spotify_auth()
        self.id = self.sp.current_user()["id"]
    
    # Generating authentication object for Spotipy API calls.
    def spotify_auth(self):
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="http://example.com",
                client_id=self.client_id,
                client_secret=self.client_secret,
                show_dialog=True,
                cache_path="token.txt"
            )
        )
        return sp
    
    # Retrieving song uris.
    def retrieve_uris(self, song_names):
        song_uris = []
        try:
            for song in song_names:
                search_results = self.sp.search(q=f"track:{song}", type="track")
                uri = search_results["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
        except IndexError:
            pass

        return song_uris
    
    # Creating Spotify playlist.
    def generate_playlist(self, date, song_names):
        playlist = self.sp.user_playlist_create(user=self.id, name=f"Best of {date}", public=False)
        self.sp.playlist_add_items(playlist_id=playlist["id"], items=self.retrieve_uris(song_names))
