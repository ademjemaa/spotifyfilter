# spotifyfilter

A spotify playlist maker through reddit top comments

HOW TO RUN:

-install both praw and spotipy with pip

-create a config file where you include the following :
{

extras =  {
    "reddit_url_id" : "example",
    "playlist_name" : "example"
}

API = {
    "client_id": "reddit client id",       
    "client_secret": "reddit client secret",
    "user_agent": "user agent title",
    "username": "reddit username",
    "password": "reddit username's password"
}

SPOTIFY ={
    "id" : "spotify client id",
    "secret" : "spotify client secret",
    "scope" : "playlist-modify-public",
    "username" : "spotify username",
    "redirect_uri" : "http://localhost"
    }
}

run reddit_fetcher.py first and then run spotify.side.py when you have your JSON file ready

To-Do List:

-make sure the same song isnt listed more than once in each playlist(WIP)

-filter out actual song names from rest of comment body perfectly(WIP)

-fix authentification token issues(prompt user to login with his spotify account on his device and export playlist to his playlists)(not even started)

-make this a callable bot on reddit (/u/spotifyfilter will fetch tracks in current thread, either on his own account or make a "spotify_filter" account that holds all playlists and returns and URL when is called)(I have 0 idea about this)
