import usersetup as myuser
import playlist as playlist # Import file
from playlist import Playlist # Import class (different from file*)

class Artist(Playlist):
    """
    Provides methods to retrieve information about an artist from my playlists.
    Attributes:
        - client_id (str): Client ID to access the Spotify API.
        - client_secret (str): Client secret to access the Spotify API.
        - playlist_id (str): The ID of the playlist from which the track is selected.
        - track_id (str): The ID of the track to retrieve artist information for.

    Methods:
        - get_artist_name(): Retrieves the name of the artist in question.
        - get_artist_id(): Obtains ID of the artist.
        - get_artist_popularity(): Obtains Spotify popularity score of the artist (0-100)
        - get_artist_top_tracks(): Returns names of the artists top 10 tracks by popularity
    """

    def __init__(self, client_id, client_secret, playlist_id, track_id):
        """
        Initialize artist object with parameters.
        """
        # Call parent class (playlist)
        super().__init__(client_id=client_id, client_secret=client_secret, playlist_id=playlist_id)

        # Set track_id for class as inputted track_id
        self.track_id = track_id

        # Extract artist id from track and save as artist_id for the class
        track_info = self.sp.track(self.track_id)
        artists = track_info['artists']
        self.artist_id = [artist['id'] for artist in artists]

    def get_artist_name(self):
        """
        Obtain name of artist who created the track.
        Returns: 
            - artist_name (str): Name of the artist.
        """
        track_info = self.sp.track(self.track_id)
        artists = track_info['artists']
        artist_name = [artist['name'] for artist in artists]
        return artist_name
    
    def get_artist_id(self):
        """
        Obtain ID of artist who created the track.
        Returns: 
            - artist_id (str): ID of the artist.
        """
        return self.artist_id
    
    def get_artist_popularity(self):
        """
        Obtain the popularity score of the artist (0-100).
        Returns: 
            - artist_popularity (int): Popularity score of the artist.
        """
        artist_popularity = []
        for artist_id in self.artist_id:
            artist_info = self.sp.artist(artist_id)
            popularity = artist_info['popularity']
            artist_popularity.append(popularity)
        return artist_popularity
    
    def get_artist_top_tracks(self):
        """
        Obtains the names of the artist's 10 top tracks.
        Returns:
            - top_tracks (array of str): The top tracks of the artist.
        """
        top_tracks = []
        for artist_id in self.artist_id:
            tracks = self.sp.artist_top_tracks(artist_id)
            top_tracks.extend([track['name'] for track in tracks['tracks']])
        return top_tracks

    def count_artist_ocurrences(self, artist_name):
        """
        Count how many times the specified artist appears in the playlist, and the percentage of the playlist they occupy
        """
        count = 0
        for item in self.get_playlist_tracks(): # USE OF PARENT METHOD
            track = item['track']
            for artist in track['artists']:
                if artist['name'] == artist_name:
                    count += 1
        return count

    def get_comparative_popularity(self, artist_name):
        """
        Return how popular the specified artist is compared to the other artists
        Parameters:
            - artist_name (str): The name of the artist to compare popularity for.
        Returns:
            - popularity_comparison (float): The popularity of the specified artist compared to others.
        """
        specified_artist_popularity = self.get_artist_popularity(artist_name)
        
        # Get all unique artists from the playlist
        unique_artists = self.get_unique_artists() # USE OF PARENT METHOD
        
        # Calculate the average popularity of all artists in the playlist
        total_popularity = sum(self.get_artist_popularity(artist) for artist in unique_artists)
        average_popularity = total_popularity / len(unique_artists)
        
        # Compare the popularity of the specified artist with the average popularity
        popularity_comparison = specified_artist_popularity / average_popularity
        
        return popularity_comparison
    
    def get_track_id_for_artist(self, artist_name):
            """
            Get the track ID for a given artist's name in the playlist.
            Parameters:
                - artist_name (str): The name of the artist to find the track ID for.
            Returns:
                - track_id (str or None): The ID of the track associated with the artist, or None if not found.
            """
            for item in self.get_playlist_tracks():
                track = item['track']
                for artist in track['artists']:
                    if artist['name'] == artist_name:
                        return track['id']
            return None     