from typing import Dict
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "CompuServe Classic/1.22",
    "Accept": "application/json",
    "Host": "api.genius.com",
    "Authorization": "Bearer ........."}
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/5"}


def get_artist_id(artist_name: str = "Kendrick Lamar", artist: bool = True):
    """Get Artist ID
    :param artist:
    :param artist_name:
    :return: Artist ID or Songs Urls
    """
    search_url = f'https://api.genius.com/search?q={artist_name}'
    search_sec_page = f'https://genius.com/api/search/song?page=2&q={artist_name}'
    req_search = requests.get(search_url, headers=headers)
    req_search_sec_page = requests.get(search_sec_page, headers=header)
    hits = req_search.json().get("response", {}).get("hits", {})
    hits_sec_page = req_search_sec_page.json().get("response", {}).get("sections")[0].get("hits", {})
    song_urls_title = {}
    if hits:
        artist_id = hits[0].get("result", {}).get('primary_artist', {})['api_path']
        for i in range(len(hits)):
            song_urls_title[hits[i].get("result", {}).get('full_title')] = hits[i].get("result", {}).get('url')
        if hits_sec_page:
            for i in range(len(hits_sec_page)):
                song_urls_title[hits_sec_page[i].get("result", {}).get('full_title')] = hits_sec_page[i].get("result", {}).get('url')
        if artist:
            return artist_id
        return song_urls_title
    else:
        if artist:
            return "/artists/16775"
        return {"I am": "https://genius.com/Jorja-smith-i-am-lyrics"}


def get_artist_song_name_list(artist_i: str = "artists/16775") -> Dict:
    """Get  list of songs name and their Urls

    :return: Songs Url and Tittle
    """
    artist_id = artist_i
    next_page = "1"
    songs_url_title = {}
    while next_page:
        url_songs = f"https://genius.com/api{artist_id}/songs?page={next_page}"
        req_songs = requests.get(url_songs, headers=headers)
        response = req_songs.json().get("response")
        next_page = response.get("next_page")
        songs = response.get("songs")
        for i in range(len(songs)):
            songs_url_title[songs[i].get("full_title")] = songs[i].get("url")
    return songs_url_title


def get_lyrics(url: str = "https://genius.com/Jorja-smith-i-am-lyrics") -> str:
    req = requests.get(url, headers=header)
    soup = BeautifulSoup(req.content, "html.parser")
    results = soup.find_all("div", {"class": "Lyrics__Container-sc-1ynbvzw-1 kUgSbL"})
    lyrics = []
    if results:
        for result in results:
            for sting in result.strings:
                if not sting.isspace():
                    lyrics.append(sting)
        lyrics = "\n".join(lyrics)
        return lyrics
    else:
        return "Pas de lyrics disponible.........Oups"
