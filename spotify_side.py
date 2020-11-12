import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
from config import SPOTIFY

token = util.prompt_for_user_token(
    username=SPOTIFY["username"],
    scope=SPOTIFY['scope'], 
    client_id=SPOTIFY["id"], 
    client_secret=SPOTIFY["secret"], 
    redirect_uri=SPOTIFY["redirect_uri"]
)

def search_query(item):
    results = sp.search(q=item, limit=3)
    while (results['tracks']['total'] == 0 and item.find('+') > 0):
        item = (item.rsplit('+', 1)[0])
        results = sp.search(q=item, limit=3)
    else :
        return (results)

sp = spotipy.Spotify(auth=token)
total = sp.user_playlist_create(SPOTIFY["username"], 'API-test1', public=True, collaborative=False, description='')
with open('data') as json_file:
    data = json.load(json_file)
    results = search_query(data[0])
    tracks = []
    for p in data:
        if len(tracks) > 100:
            break
        results = search_query(p)
        for idx, track in enumerate(results['tracks']['items']):
            if not 'Remix' in track['name']:
                tracks.append(track['uri'])
                break
sp.playlist_add_items(total['id'], tracks, position=None)