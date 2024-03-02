import sys
from HFAuth import HFAuth
from HFBytes import HFBytes

def main():
    if len(sys.argv) < 4:
        print("Usage: python sendBytesCLI.py <uid> <num_bytes> <reason>")
        sys.exit(1)

    uid = sys.argv[1]
    num_bytes = sys.argv[2]
    reason = ' '.join(sys.argv[3:])

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

    # Send bytes
    success, response = hf_bytes.send_bytes(uid, num_bytes, reason)

    if success:
        print("Bytes sent successfully.")
    else:
        print(f"Error sending bytes: {response}")

if __name__ == "__main__":
    main()
