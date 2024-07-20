import usersetup as myuser
import playlist as playlist # Import file
from playlist import Playlist # Import class

class Song(Playlist):
    """
    Represents a song and provides methods to retrieve its audio features and album name.
    Attributes:
        - client_id (str): Client ID to access the Spotify API.
        - client_secret (str): Client secret to access the Spotify API.
        - playlist_id (str): ID of the playlist the selected track is in.
        - track_id (str): The ID of the track to retrieve information for.
        - audio_features (dict/array): A list of the audio features of the track.

    Methods:
        - trim_audio_features(): Retrieves a list of modified audio features for the track.
        - get_album(): Obtains the album name that the song is from.
    """

    def __init__(self, client_id, client_secret, playlist_id, track_id):
        """
        Initialize a Song object with given parameters.
        """
        # Call parent class (playlist)
        super().__init__(client_id=client_id, client_secret=client_secret, playlist_id=playlist_id)

        # Set track_id for class as inputted track_id
        self.track_id=track_id
        # Set an empty variable that will hold the audio features once called/initialized
        self.audio_features = None

    def trim_audio_features(self):
        """
        Obtains the audio features of the track.
        Returns:
            - audio_features (dict/array): The audio features of the track.
        """
        audio_features = (self.sp.audio_features(self.track_id))[0]

        # *Filter out the list of audio features so it's in identical format to my dataframe
        filtered = {key: value for key, value in audio_features.items() if key not in ('type', 'id', 'uri', 'track_href', 'analysis_url')}
        filtered ['duration_ms'] //= 1000
        # Set audio features for class equal to the filtered set
        self.audio_features = filtered
        return self.audio_features
    
    def get_album(self):
        """
        Obtains the album name of the track.
        Returns:
            - album_name (str): The album name of the track.
        """
        track_info = self.sp.track(self.track_id)
        album_name = track_info['album']['name']
        return album_name


'''
for track in userplaylist:
    print(track['id'])

     # Convert numbers into actual key - Number to String
        key_mapping = {0:'C', 1:'C#', 2:'D', 3:'D#', 4:'E', 5:'F', 6:'F#', 7:'G', 8:'G#', 9:'A', 10:'A#', 11:'B'}
        filtered['key'] = filtered['key'].map(key_mapping)
        # Convert numbers to Major/Minor - Number to String
        filtered['mode'] = filtered['mode'].apply(lambda x: 'Major' if ((x%2) == 0) else 'Minor') 

'''

