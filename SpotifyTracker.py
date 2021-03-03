import spotipy
import sys
import spotipy.util as util
import time
from spotipy.oauth2 import SpotifyOAuth

class APImanager:
    def __init__(self):
        scope = "user-read-currently-playing user-read-playback-state user-read-playback-position user-follow-read"

        username = 'OctaneMR'
        SPOTIPY_CLIENT_ID='70556e1830db4dd687adce562f4b9124'
        SPOTIPY_CLIENT_SECRET='b6d2a399476e496ba1f27fd7bdbd0c4f'
        SPOTIPY_REDIRECT_URI='http://localhost/'

        token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
        self.sp = spotipy.Spotify(auth=token)

# returns current track name
    def getCurrentTrack(self):
        results = self.sp.current_playback()
        print(results)
        if results is not None:
            item = results['item']
            return item['name']
        else:
            return None

# returns current track artist
    def getCurrentArtist(self):
        results = self.sp.current_playback()
        if results:
            item = results['item']
            artist = item["artists"][0]
            return artist['name']
        else:
            return None

# returns previous track name
    def getPreviousTrack(self):
        results = self.sp.current_playback()
        if results:
            item = results['item']
            artist = item["artists"][0]
            return artist['name']
        else:
            return None

test = APImanager()
print(test.getCurrentArtist())

    
