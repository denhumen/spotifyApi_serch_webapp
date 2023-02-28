"""
Script works with
SPotify API and helps
users with finding
information about artists
"""

import os
import base64
import json
from typing import List
import pycountry
import folium
from pathlib import Path
from requests import post, get
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = os.path.join(BASE_DIR, 'templates', "main")

def get_token():
    """
    Function
    """
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    """
    Functiion
    """
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    """
    Function
    """
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        return None
    return json_result[0]

def get_songs_by_artist(token, artist_id):
    """
    Function
    """
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)['tracks']
    return json_result

def get_available_markets(token: str, song_id: str):
    """
    Function
    """
    url = f"https://api.spotify.com/v1/tracks/{song_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result['available_markets']

def iso_to_name(iso_list: List[str]) -> List[str]:
    """
    Function
    """
    countries = []
    for iso in iso_list:
        country = pycountry.countries.get(alpha_2=iso)
        try:
            countries.append(country.name)
        except Exception:
            continue
    return countries

def colorPicker(name, countries):
        if name in countries:
            return 'green'
        else:
            return 'red'

def create_map(artist_name: str):
    """
    Function
    """
    token = get_token()
    result = search_for_artist(token, artist_name)
    if result == None:
        return None
    else:
        artist_id = result["id"]
        songs = get_songs_by_artist(token, artist_id)
        iso_list = get_available_markets(token, songs[0]['id'])
        countries = iso_to_name(iso_list)
    m = folium.Map(location=[32, 0],
               zoom_start=4.3,
               tiles = "CartoDB positron",
               min_zoom=3,
               max_zoom=18,
               max_bounds=True)
    folium.GeoJson(open('main/scripts/population.json', 'r', encoding='utf-8-sig').read(),
                name = 'Population',
                style_function = lambda x: {'fillColor': colorPicker(x['properties']['NAME'], countries), 'weight': 0.5},
                show = False,
                zoom_on_click=True).add_to(m)
    print(STATIC_ROOT)
    m.save(f"{STATIC_ROOT}\map.html")