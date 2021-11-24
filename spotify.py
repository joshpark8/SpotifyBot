import requests
import json

base_url = 'https://api.spotify.com/v1/'

'''
This function uses my personal client ID and client secret to
authenticate to spotify that I have permission to use their API.
It also uses an HTTP post to fetch and return the access token.
'''
def auth():
    cid = '81e4cc229b3b48388283926b652c2464'
    secret = '8565ec9a7cbe4487bbd6834f3eea4ac2'
    auth_url = 'https://accounts.spotify.com/api/token'
    r = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': cid,
        'client_secret': secret,
    })
    auth_response_data = r.json()
    access_token = auth_response_data['access_token']
    headers = {
        'Authorization': 'Bearer {token}'.format(token = access_token)
    }
    return headers

'''
This function uses the access token along with the user's specified
artist name to access the Spotify API and retrieve the artist ID.
'''
def get_artist_id(content):
    headers = auth()
    artist = '%20'.join(content.split()[1:])
    r = requests.get(base_url + 'search?q=' + artist + '&type=album&limit=1', headers = headers)
    r = r.json()
    json_formatted_str = json.dumps(r, indent=2) #
    print(json_formatted_str) #
    if len(r['albums']['items']) == 0:
        return -1
    return r['albums']['items'][0]['artists'][0]['id']

'''
This function fetches the artist's name
'''
def get_artist_name(artist_id, headers):
    r = requests.get(base_url + 'artists/' + artist_id, headers = headers)
    artist = r.json()
    json_formatted_str = json.dumps(r, indent=2) #
    print(json_formatted_str) #
    return artist['name']
    
'''
This function fetches the follower count for the artist.
'''
def followers(content):
    artist_id = get_artist_id(content)
    headers = auth()
    if artist_id == -1:
        return -1
    
    r = requests.get(base_url + 'artists/' + artist_id, headers = headers)
    artist = r.json()
    json_formatted_str = json.dumps(r, indent=2) #
    print(json_formatted_str) #
    artist_name = get_artist_name(artist_id, headers)
    follow_count = artist['followers']['total']
    return artist_name + ' has ' + str(follow_count) + ' followers'

'''
This function fetches the top 10 songs for the artist.
'''
def topSongs(content):
    artist_id = get_artist_id(content)
    headers = auth()
    if artist_id == -1:
        return -1
    
    r = requests.get(base_url + 'artists/' + artist_id + '/top-tracks?market=US&limit=10', headers = headers)
    top_tracks = r.json()
    json_formatted_str = json.dumps(r, indent=2) #
    print(json_formatted_str) #
    artist_name = get_artist_name(artist_id, headers)
    song_names = []
    for track in top_tracks['tracks']:
        song_names.append(track['name']) 
    songs = '\n'.join(song_names)
    return artist_name + "'s top songs are:\n" + songs

'''
This function fetches up to 20 similar artists
'''
def related(content):
    artist_id = get_artist_id(content)
    headers = auth()
    if artist_id == -1:
        return -1
    
    r = requests.get(base_url + 'artists/' + artist_id + '/related-artists', headers = headers)
    related_artists = r.json()
    json_formatted_str = json.dumps(r, indent=2) #
    print(json_formatted_str) #
    artist_name = get_artist_name(artist_id, headers)
    artist_names = []
    for artist in related_artists['artists']:
        artist_names.append(artist['name'])
    artist_names = artist_names[:10]
    artists = '\n'.join(artist_names)
    return "Artists related to " + artist_name + " are:\n" + artists

'''
This function fetches the artists top 10 albums
'''
def albums(content):
    artist_id = get_artist_id(content)
    headers = auth()
    if artist_id == -1:
        return -1
    
    r = requests.get(base_url + 'artists/' + artist_id + '/albums?limit=10', headers = headers)
    albums = r.json()
    json_formatted_str = json.dumps(r, indent=2) #
    print(json_formatted_str) #
    artist_name = get_artist_name(artist_id, headers)
    album_names = []
    for album in albums['items']:
        album_names.append(album['name'])
    album_ret = '\n'.join(album_names)
    return artist_name + "'s top 10 albums are are:\n" + album_ret
