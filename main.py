import billboard
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
client_id = "dc30966bea0c499a9368a50acb8ac48f"
client_secret = "e40f2adf929345d4b43a107d5bb7a3fd"
redirect_uri = "http://localhost:8888/callback"

# Spotify username
username = input("Enter your Spotify username: ")

# Authenticate with Spotify
scope = "playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# Billboard top 100 songs list
chart = billboard.ChartData('hot-100')
top100_list = []
for i in range(100):
    top100_list.append(chart[i])

# Create a new playlist on Spotify
playlist_name = "Billboard Top 100"
playlist_description = "Automatically generated playlist with the current top 100 songs from Billboard"

playlist = sp.user_playlist_create(user=username, name=playlist_name, public=False, description=playlist_description)

# Add tracks to the playlist
tracks = []
for song in top100_list:
    song_title = song.title
    artist_name = song.artist
    query = f"track:{song_title} artist:{artist_name}"
    results = sp.search(q=query, type="track")
    if results["tracks"]["total"] > 0:
        track_id = results["tracks"]["items"][0]["id"]
        tracks.append(track_id)

sp.user_playlist_add_tracks(user=username, playlist_id=playlist["id"], tracks=tracks)

print(f"Playlist created: {playlist_name} ({playlist['id']})")
print(f"Tracks added to playlist: {playlist_name}")