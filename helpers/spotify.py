import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIFY_ID, SPOTIFY_SECRET

def get_spotify():
    if not SPOTIFY_ID or not SPOTIFY_SECRET:
        return None
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET
    ))

def resolve_spotify(url: str):
    sp = get_spotify()
    if not sp:
        return url
    if "track" in url:
        track = sp.track(url)
        name = track["name"]
        artist = track["artists"][0]["name"]
        return f"{name} {artist}"
    elif "playlist" in url:
        results = sp.playlist_tracks(url)
        queries = []
        for item in results["items"]:
            t = item["track"]
            queries.append(f"{t['name']} {t['artists'][0]['name']}")
        return queries
    return url
