#1 A random Spotify track ID
import urllib.request
import json

url='https://j72ajh.deta.dev/spotify_id'
data=urllib.request.urlopen(url).read().decode()
sp_ID=json.loads(data) 
print(sp_ID)

#2
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id="c48da9d3dde74e8db6e689eb102768f2"
client_secret="c94d02b2971e49c58891493231f7843d"

track_ID=sp_ID['spotify_id'] #Get ID
sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id,client_secret))
result = sp.track(track_ID) 

#js=json.dumps(result)

track=result["name"]
artists=''
count=0 
for artist in result["artists"]: 
        if artists!='': #If artists has letter
            artists+=', '
        artists+=artist["name"] #Use string 
   

album=result["album"]["name"] 
link=result["external_urls"]["spotify"]

#Answer
print('Track: ',track)
print('Artists: ',artists)
print('Album: ',album)
print('Link: ',link)











