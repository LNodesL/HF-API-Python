from flask import Flask, request, redirect, render_template_string
from HFAuth import HFAuth  # Adjust import according to your project structure
from HFBytes import HFBytes 

app = Flask(__name__)

@app.route('/callback')
def callback():
    # Extract authorization code and state from the query parameters
    auth_code = request.args.get('code', None)
    state = request.args.get('state', None)

    if auth_code and state:
        # Instantiate your HFAuth class
        # Note: Ensure HFAuth is configured to use the correct port, potentially this app's port + 1
        auth = HFAuth()
        
        # Handle the token exchange with the provided code and state
        auth.handle_token_exchange(auth_code, state)
        
        # Attempt to retrieve the token after exchange
        token = auth.get_token()
        if token:
            # If token exists, redirect to a success page or another route that requires authentication
            return redirect('/success')
        else:
            # If no token is found, perhaps redirect back to login or another attempt to authenticate
            return redirect('/install')
    else:
        # If no auth_code or state does not match, handle the error (e.g., show an error message or log it)
        return "Error: Authorization failed or state does not match."


@app.route('/install')
def install():
    auth = HFAuth()
    # token = auth.get_token()
    # if token:
    #     # If token exists, redirect to a success page or another route that requires authentication
    #     return redirect('/success')
    # else:
    #     # If no token is found, perhaps redirect back to login or another attempt to authenticate
    #     return redirect('/install')
    authorization_url = f"{auth.HF_API_URL_AUTHORIZE}?response_type=code&client_id={auth.CLIENT_ID}&state={auth.STATE}&redirect_uri={auth.REDIRECT_URI}"
    return redirect(authorization_url)

@app.route('/success')
def success():
    return "Successfully connected to HF API. Make sure your IP is whitelisted to continue using Python tools.<br />Use the sendBytesCLI.py or sendBytesStatic.py file to get started. Check out readme.md for more info!<br /><a href='/send-bytes'>Send Bytes Form</a>"


# HTML template for the form
FORM_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Send Bytes</title>
</head>
<body>
    <h2>Send Bytes Form</h2>
    <form method="post" action="/send-bytes">
        UID: <input type="text" name="uid"><br>
        Amount of Bytes: <input type="number" name="num_bytes"><br>
        Reason: <input type="text" name="reason"><br>
        <input type="submit" value="Send Bytes">
    </form>
</body>
</html>
"""

@app.route('/send-bytes', methods=['GET'])
def form():
    return render_template_string(FORM_TEMPLATE)

@app.route('/send-bytes', methods=['POST'])
def send_bytes():
    uid = request.form['uid']
    num_bytes = request.form['num_bytes']
    reason = request.form['reason']

    # Initialize HFAuth to get the access token
    hf_auth = HFAuth()
    token_info = hf_auth.get_token()

    if not token_info:
        return "You are not currently authenticated. Please authenticate via your web browser on your /install route on the IP/address from server.py or manually install (python install.py).", 401
    
    # Extract the access token
    access_token = token_info.get('access_token')
    
    if not access_token:
        return "Failed to retrieve access token.", 500

    # Initialize HFBytes with the obtained access token
    hf_bytes = HFBytes(access_token)

    # Send bytes
    success, response = hf_bytes.send_bytes(uid, num_bytes, reason)

    if success:
        return "Bytes sent successfully."
    else:
        return f"Error sending bytes: {response}", 500

if __name__ == "__main__":
    app.run(port=8000)
