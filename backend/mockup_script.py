from flask import Flask, jsonify, request 
from flask_cors import CORS
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import dev.spotAPI_base
import dev.spotAPI_minehelper
import dev.spotAPI_minedata
import dev.spotAPI_recSystem
from dev.spotAPI_recSystem import get_recs

app = Flask(__name__, static_folder='static')
cors = CORS(app, origins='*')

# Spotify API setup (assuming credentials are in environment variables)
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#this is an example to see how a python script would send data to the frontend
#if you are trying to run this, make sure to use a virtual environment! :) 
#note: the following commands are for windows
# python3 -m venv virtual_environment
#activate with this command: virtual_environment/Scripts/activate
#to run the script do: python mockup_script.py
#you can see the returned JSON on http://localhost:8080/api/users
@app.route("/api/users", methods = {'GET'})

def get_songs():
    song_name = request.args.get('song_name')

    if not song_name:
        return jsonify({"error": "Please provide a song name"}), 400

    result = get_recs(song_name)
    
    return jsonify(
        {
            "songs": [
                {
                    "song_name": row["Track Name"],
                    "artist": row["Artist"],
                    "album_cover": row["Thumbnail URL"]
                }
                for _, row in result.iterrows()
            ]
        }
    )

if __name__ == "__main__":
    app.run(debug=True, port=8080)
