import spotipy
from spotipy import SpotifyOAuth
import os
import urllib.request

SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''
SPOTIPY_REDIRECT_URI = ''
SCOPE = "user-read-playback-state,user-modify-playback-state, user-library-read"
CACHE = '.spotipyoauthcache'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = SPOTIPY_CLIENT_ID, client_secret = SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))

if not os.path.exists("covers"):
    os.mkdir("covers")

offset = 0
limit = 50
all_saved_albums = []

while True:
    results = sp.current_user_saved_albums(limit=limit, offset=offset)
    saved_albums = results['items']
    all_saved_albums.extend(saved_albums)
    if len(saved_albums) < limit:
        break
    offset += limit

for album in all_saved_albums:
    album_id = album['album']['id']
    album_details = sp.album(album_id)
    cover_url = album_details['images'][0]['url']
    file_name = "covers/" + album_details['id'] + ".jpg"
    urllib.request.urlretrieve(cover_url, file_name)