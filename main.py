import usersetup as myuser
from usersetup import UserSetup

from playlist import Playlist

from artist import Artist
from song import Song

'''
Code from my playlist file
'''
# Set playlist ID to my main
playlist_id = "4WvAhmKvRMm17BoTTdJ93b"
instrumental_id = "1nY9RRf2cPY9Hzf8eDkAY8"

# friend_playlist_id = "5X3l9NxSiSwjRYBaikHqac"
# https://open.spotify.com/playlist/79QLI3G5Cl6VOXYy1Z7sCA?si=5VbvuiTISmWQH6u7MvnvMQ&pi=u-4bs_JOE1Q4yS

# Create object
myPlaylist = Playlist(myuser.client_id,myuser._client_secret,playlist_id=playlist_id)
instrumentalPlaylist = Playlist(myuser.client_id,myuser._client_secret,playlist_id=instrumental_id)

# Retrieve tracks from the specified playlist
playlist_tracks = myPlaylist.get_playlist_tracks()
myPlaylist.print_playlist_info()
print(playlist_tracks[0])

#instrumentalPlaylist.get_playlist_info()


print("Owner Name:", myPlaylist.get_owner_name())
print(myPlaylist.get_total_tracks())
# allplaylists = Playlist.get_current_user_playlists()
# allplaylists = Playlist.get_user_playlists(_user_id)



'''
Code from my artist file
'''
all_artists = []
# Iterate through the tracks and extract the artists' names
for item in playlist_tracks:
    track = item['track']
    for artist in track['artists']:
        all_artists.append(artist['name'])

# Remove duplicate artists if any
all_artists = list(set(all_artists))
print("Total Number of Different Artists:", len(all_artists))
print(all_artists[0:3])

#--------------------------------------------------------------------

## RECURSION
def get_artist_popularity(artist_names, artist_popularity = {}):

    # Base case - If no more artists to process, return artist popularity list
    if not artist_names:
        return artist_popularity
    
    # Process the next artist
    artist_name = artist_names.pop()
    track_id = artist.get_track_id_for_artist(artist_name)
    artist_instance = Artist(myuser.client_id, myuser._client_secret, playlist_id, track_id)
    popularity = artist_instance.get_artist_popularity()[0]  # neglects features
    artist_popularity[artist_name] = popularity

    # Call function again (recursion) to process remaining artists
    return get_artist_popularity(artist_names, artist_popularity)


artist_popularity = get_artist_popularity(set(all_artists))


# sort the dictionary and print
sorted_artists = sorted(artist_popularity.items(), key=lambda x: x[1], reverse=True)
for artist, popularity in sorted_artists:
    print(f"{artist}: Popularity - {popularity}")

# Example track to analyze artist - Blinding Lights by the Weeknd
track_id = "0VjIjW4GlUZAMYd2vXMi3b" 

# Initialize object and call function methods
firstArtist = Artist(myuser.client_id, myuser._client_secret, playlist_id, track_id)
print(firstArtist.get_artist_name())
print(firstArtist.get_artist_popularity())
print(firstArtist.get_artist_id())
print(firstArtist.get_artist_top_tracks())



'''
Code from my song file
'''

# Obtain the userplaylist and id from the playlist file
userplaylist = myPlaylist
mainplaylist_id = playlist_id
tracks = userplaylist.get_playlist_tracks()
track_ids = [item['track']['id'] for item in tracks]

# Create new song instance for each song in playlist
trimmed_tracks = track_ids[0:3]
characteristics = []
for track in trimmed_tracks:
    songx = Song(myuser.client_id, myuser._client_secret, mainplaylist_id, track)
    characteristics.append(songx.trim_audio_features())

print(characteristics)


# Define two track ids
track_id = "0VjIjW4GlUZAMYd2vXMi3b"
instrumentaltrack_id = "0w7yUSxpQV3a3HqlprOQUs"

# Create two instances of the song object
firstsong = Song(myuser.client_id, myuser._client_secret, mainplaylist_id, track_id)
firstsongalt = Song(myuser.client_id, myuser._client_secret, instrumental_id, instrumentaltrack_id)

# Get audio features of the second song
trialsongfeatures = firstsongalt.trim_audio_features()
# print(trialsongfeatures)

# Get album of the first song
print(firstsong.get_album())

