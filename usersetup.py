import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

# Declare valuable of variables 
client_id = "0a3c9346f6f142c09f338959b8c1d24b"
_client_secret = "51ddcd96c8224e749ba1dff19c4dfb77"
_user_id = "ktg000lpqkt06fd9gjmfepfcr"

class UserSetup:
    def __init__(self, client_id, client_secret):
        """
        Represents the setup for a Spotify user, including authentication and API access.
        Attributes:
            - client_id (str): The client ID for accessing the Spotify API.
            - client_secret (str): The client secret for accessing the Spotify API.
            - sp (spotipy.Spotify): Instance of the spotipy.Spotify class initialized with the client credentials manager.
        """
        scope = "user-library-read"
        # Set up the Spotify client credentials manager for authentication
        self.client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=_client_secret)
        # Initialize a Spotify client object for API access
        self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager) 
        self.client_id = client_id
        self.client_secret = client_secret
