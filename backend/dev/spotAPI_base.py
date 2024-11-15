import os
from dotenv import load_dotenv

import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

load_dotenv()
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

metadata_headers = [
    "Track Name",
    "Artist",
    "Album",
    "Thumbnail URL",
    "id",
    "uri",
    "track_href",
    "analysis_url",
    "type",
]

audio_headers = [
    "danceability",
    "energy",
    "key",
    "loudness",
    "mode",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
    "tempo",
    "duration_ms",
    "time_signature"
]

csv_headers = metadata_headers + audio_headers + ["sin_key"]