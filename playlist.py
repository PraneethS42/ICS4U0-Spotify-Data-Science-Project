import usersetup as myuser
from usersetup import UserSetup

class Playlist(UserSetup):
    """
    Class for a Spotify playlist: Provides methods to retrieve information about the playlist.
    Attributes:
        - client_id (str): Client ID to access the Spotify API.
        - client_secret (str): Client secret to access the Spotify API.
        - playlist_id (str): ID of the playlist the selected track is in.
        - all_tracks (array): ID of the playlist the selected track is in.

    Methods:
        - get_playlist_tracks(): Retrieves a list of tracks from the playlist.
        - _get_playlist_info(): Obtains all information about the playlist.
        - print_playlist_info(): Prints information about the playlist.
        - _get_owner_name(): Getter method for the owner's name.
        - get_total_tracks(): Getter method for the number of tracks in the playlist.
    """

    def __init__(self, client_id, client_secret, playlist_id): 
        """
        Initializes a Playlist object with the provided parameters.
        Parameters:
            - client_id (str): Client ID for accessing the Spotify API.
            - client_secret (str): Client secret for accessing the Spotify API.
            - playlist_id (str): The ID of the playlist.
        """
        # Call the usersetup initialization
        super().__init__(client_id=client_id, client_secret=client_secret)
        # Placeholder for playlist info, PRIVATE
        self._playlist_info = self.sp.playlist(playlist_id) 
        self.playlist_id = playlist_id
        self.all_tracks = []
    
    def __get_playlist_info(self):
        """
        Retrieves all info about the playlist.
        Returns:
            - playlist_info (dict): Dictionary/array containing information about the playlist.
        """
        # self._playlist_info = self.sp.playlist(playlist_id)
        return self._playlist_info

    def print_playlist_info(self): 
        """
        Prints pertinent info about the playlist.
        """
        playlist_info = self.__get_playlist_info()
        print(f"Playlist Name: {playlist_info['name']}")
        print(f"Owner: {playlist_info['owner']['display_name']}")
        print(f"Total Tracks: {playlist_info['tracks']['total']}")
        print(f"Public: {'Yes' if playlist_info['public'] else 'No'}")
        print(f"Collaborative: {'Yes' if playlist_info['collaborative'] else 'No'}")
        print(f"Description: {playlist_info['description']}")

    def get_owner_name(self):
        """
        Getter method for the owner's name.
        Returns:
            - owner_name (str): The owner's name.
        """
        if self._playlist_info is None:
            return None
        return self._playlist_info['owner']['display_name']
    
    def get_total_tracks(self):
        """
        Getter method for the number of tracks in the playlist.
        Returns:
            - total_tracks (int): The number of tracks in the playlist.
        """
        if self._playlist_info is None:
            return None
        return self._playlist_info['tracks']['total']
    
    def get_playlist_tracks(self):
        """
        Retrieves tracks from the specified playlist.
        Returns:
            - all_tracks (list): List containing information about all tracks in the playlist.
        """
        # Initialize empty list to store all tracks
        # Spotify API can only request 100 songs at a time, retrieve tracks in batches of 100 until all tracks are fetched
        offset = 0
        while True:
            tracks_batch = self.sp.playlist_tracks(self.playlist_id, offset=offset)
            # Add batch of 100 to current
            self.all_tracks.extend(tracks_batch['items'])
            # Update offset for next group
            offset += len(tracks_batch['items'])
            # Break loop if none left
            if len(tracks_batch['items']) < 100:
                break
        return self.all_tracks

    def get_unique_artists(self):
        """
        Get a list of unique artists from the playlist.
        Returns:
            - unique_artists (list): List of unique artist names.
        """
        unique_artists = set()
        for item in self.get_playlist_tracks():
            track = item['track']
            for artist in track['artists']:
                unique_artists.add(artist['name'])
        return list(unique_artists)
