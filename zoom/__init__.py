import requests
from base64 import b64encode
from .user_details_extractor import ExtractUserDetails
from .meeting_details_extractor import ExtractMeetingDetails
import os

class ZoomExtractor:
    def _get_zoom_service(self):
        client_id = os.environ.get('ZOOM_CLIENT_ID')
        client_secret = os.environ.get('ZOOM_CLIENT_SECRET')
        account_id = os.environ.get('ZOOM_ACCOUNT_ID')
        # Encode the client ID and client secret
        credentials = f"{client_id}:{client_secret}"
        encoded_credentials = b64encode(credentials.encode()).decode('utf-8')

        # Construct the URL
        url = f"https://zoom.us/oauth/token?grant_type=account_credentials&account_id={account_id}"

        # Set the headers
        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/json"
        }

        # Make the POST request
        response = requests.post(url, headers=headers)
        token_response = response.json()
        # Return the response
        return token_response['access_token']

    def _get_user_details_seervice(self, user_id):
        access_token = self._get_zoom_service()
        # Construct the URL
        url = f"https://api.zoom.us/v2/users/{user_id}"

        # Set the headers
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        # Make the GET request
        response = requests.get(url, headers=headers)

        # Return the response
        return response.json()

    def get_meeting_details(self, user_id):
        access_token = self._get_zoom_service()
        # Construct the URL
        url = f"https://api.zoom.us/v2/users/{user_id}/meetings"

        # Set the headers
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        # Make the GET request
        response = requests.get(url, headers=headers)

        # Return the response
        return response.json()

    def _get_meeting_details_by_meeting_id(self, meeting_id):
        access_token = self._get_zoom_service()
        # Construct the URL
        url = f"https://api.zoom.us/v2/meetings/{meeting_id}"

        # Set the headers
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        # Make the GET request
        response = requests.get(url, headers=headers)

        # Return the response
        return response.json()
