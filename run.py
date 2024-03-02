from hfauth import HFAuth  # Ensure HFAuth is imported correctly

def main():
    hf_auth = HFAuth()  # Instantiate HFAuth

    token = hf_auth.get_token()  # Attempt to retrieve a token

    # Check if token exists and matches the expected UID
    if token and token.get('uid') == HFAuth.TOKEN_UID:
        print("Success: This application is currently connected to HF servers and the access token matches the system owner UID.")
    else:
        print("Failure: This application is not connected to HF servers at this time.")

if __name__ == "__main__":
    main()
