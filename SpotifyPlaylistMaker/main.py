from playlist_creator import PlaylistCreator
from song_generator import SongGenerator

song_generator = SongGenerator()
playlist_creator = PlaylistCreator()
playlist_creator.generate_playlist(song_generator.playlist_date, song_generator.get_songs())










