import webbrowser
import sys
from HFAuth import HFAuth

# Assuming HFAuth and other configurations are set with static variables as discussed
hf_auth = HFAuth()

token = hf_auth.get_token()

if token:
    # Instead of redirecting, inform the user to open the dashboard manually or automate this in future versions
    print("You are already authenticated to use the HF API from your current system.")
else:
    # Construct the authorization URL
    authorization_url = f"{hf_auth.HF_API_URL_AUTHORIZE}?response_type=code&client_id={hf_auth.CLIENT_ID}&state={hf_auth.STATE}&redirect_uri={hf_auth.REDIRECT_URI}"
    
    # Prompt the user to open the URL in their default browser
    print("You are not currently authenticated. Please authenticate via your web browser.")
    print("Opening authentication page...")
    webbrowser.open(authorization_url)
