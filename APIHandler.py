import spotipy
import sys
import spotipy.util as util
import time
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv


# create API handler to manager API calls
class APIHandler:
    def __init__(self):
        # define scope for user admitted permissions
        scope = "user-read-currently-playing" 
        scope += " user-read-playback-state"
        scope += " user-read-playback-position" 
        scope += " user-follow-read" 
        scope += " user-modify-playback-state"

        # load environmental variables for api keys
        load_dotenv()
        # spotify account username
        SPOTIFY_USERNAME = os.environ.get('SPOTIFY_USERNAME')
        # spotify application id and secret
        SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
        SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
        # redirect url
        SPOTIPY_REDIRECT_URI='http://localhost/'
        # create token for application access
        token = util.prompt_for_user_token(SPOTIFY_USERNAME,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
        self.sp = spotipy.Spotify(auth=token)

# returns current track name
    def getCurrentTrack(self):
        results = self.sp.current_playback()
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

# skips to next track
    def nextTrack(self):
        self.sp.next_track()

# go to previous track
    def previousTrack(self):
        self.sp.previous_track()

# returns playback state 
    def isPlaying(self):
        results = self.sp.current_playback()
        return results["is_playing"]

# stop or resume playback   
    def playPause(self):
        if self.isPlaying():
            self.sp.pause_playback()
        else:
            self.sp.start_playback()

# return url of current track cover art
    def getCoverArt(self):
        results = self.sp.current_playback()
        item = results['item']
        album = item['album']
        images = album['images']
        return images[1]['url']

# return track popularity (integer value 0-100)   
    def getTrackPopularity(self):
        results = self.sp.current_playback()
        item = results['item']
        return item['popularity']