import sys
from HFAuth import HFAuth
from HFBytes import HFBytes

def main():

    # Initialize HFAuth to get the access token
    hf_auth = HFAuth()
    token_info = hf_auth.get_token()

    if not token_info:
        print("You are not currently authenticated. Please authenticate via your web browser on your /install route on the IP/address from server.py or manually install (python install.py).")
        sys.exit(1)
    
    # Extract the access token
    access_token = token_info.get('access_token')
    
    if not access_token:
        print("Failed to retrieve access token.")
        sys.exit(1)

    # Initialize HFBytes with the obtained access token
    hf_bytes = HFBytes(access_token)

    uid = 5343398 # send to a HF UID (4931690 = nodes, 1 = Omni, etc)
    num_bytes = 5 # send 5 bytes
    reason = 'Sending bytes from Python testing script'

    # Send bytes
    success, response = hf_bytes.send_bytes(uid, num_bytes, reason)

    if success:
        print("Bytes sent successfully.")
    else:
        print(f"Error sending bytes: {response}")

if __name__ == "__main__":
    main()
