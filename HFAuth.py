import requests
import json
import time
from pathlib import Path
from hf_config import HF_API_URL, CLIENT_ID, SECRET_KEY  # Import shared configurations

class HFAuth:
    # Static variables specific to HFAuth
    HF_API_URL = HF_API_URL
    HF_API_URL_AUTHORIZE = f"{HF_API_URL}authorize"
    TOKEN_FILE_PATH = "tmp/accessToken"
    STATE = "authStateVariableDemo"
    REDIRECT_URI = "http://127.0.0.1:8001/callback"
    CLIENT_ID = CLIENT_ID
    SECRET_KEY = SECRET_KEY

    def __init__(self):
        self.token_file_path = Path(self.TOKEN_FILE_PATH)

    def post_request_with_requests(self, url, data, http_headers=None):
        headers = http_headers if http_headers else {}
        response = requests.post(url, data=data, headers=headers)
        return response.text, response.status_code

    def save_token_to_file(self, tokens):
        tokens['expire_time'] = time.time() + tokens['expires_in']
        with self.token_file_path.open('w') as f:
            json.dump(tokens, f)

    def read_token_from_file(self):
        if self.token_file_path.exists():
            try:
                with self.token_file_path.open() as f:
                    return json.load(f)
            except json.JSONDecodeError:
                # Handle empty or invalid JSON
                print("The token file is empty or contains invalid JSON.")
                return None
        return None

    def handle_token_exchange(self, authorization_code, state):
        if self.STATE == self.STATE:  # Simplified for the example; adjust as needed
            if authorization_code:
                post_data = {
                    'grant_type': 'authorization_code',
                    'client_id': self.CLIENT_ID,
                    'client_secret': self.SECRET_KEY,
                    'code': authorization_code,
                }

                response, http_status_code = self.post_request_with_requests(self.HF_API_URL_AUTHORIZE, post_data)

                if http_status_code == 200:
                    tokens = json.loads(response)
                    self.save_token_to_file(tokens)
                    print("Authorization successful! Tokens received and saved.")
                else:
                    print(f"Error exchanging code for tokens. HTTP status code: {http_status_code}")
            else:
                print("Authorization code is missing.")
        else:
            print("Invalid state parameter.")

    def get_token(self):
        existing_token = self.read_token_from_file()
        if existing_token and existing_token['expire_time'] > time.time():
            return existing_token
        return None
