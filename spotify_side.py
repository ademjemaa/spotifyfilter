import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIFY

def search_query(item):
    results = sp.search(q=item, limit=2)
    while (results['tracks']['total'] == 0 and item.find('+') > 0):
        item = (item.rsplit('+', 1)[0])
        results = sp.search(q=item, limit=3)
    else :
        return (results)

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY["id"],
                                                           client_secret=SPOTIFY["secret"]))
with open('data') as json_file:
    data = json.load(json_file)
    results = search_query(data[0])
    tracks = []
    for p in data:
        results = search_query(p)
        for idx, track in enumerate(results['tracks']['items']):
            if not 'Remix' in track['name']:
                tracks.append(track['uri'])
                break