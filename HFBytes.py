import requests
from hf_config import HF_API_URL  # Import shared configuration

class HFBytes:
    def __init__(self, access_token):
        self.access_token = access_token
        self.write_url = f"{HF_API_URL}write/bytes"  # Use the shared HF API URL

    def send_bytes(self, uid, amount, reason):
        payload = {
            'asks': {
                'bytes': {
                    '_uid': uid,
                    '_amount': amount,
                    '_reason': reason,
                },
            },
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.access_token}',
        }
        response = requests.post(self.write_url, json=payload, headers=headers)
        if not response.ok:
            return False, response.text
        return True, response.json()

    def get_last_error(self):
        # Implement according to your error handling logic
        pass
