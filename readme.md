# HF API Python

Useful functions for authenticating with HF API and sending bytes.

## Edit 'hp_config.py' File
- You must have your own client id and secret from HackForums.net
- Once your app is approved by staff, go back to your app in HF, click 'Edit' and add your personal or server IP to the whitelist field
- You cannot use this library until you have your client id / secret and have added your IP to the whitelist
- This library uses a flask server for the auth callback URL. After that you can use the HFAuth and HFBytes classes in any valid Python code



## Run the server first
```
python server.py
```
The server is used for:
- receive HF app permission callback / redirect URI
- /install web route to get started (optional)
- /send-bytes web form

Access token is cached after you successfully complete install process.
- seen in tmp/accessToken file

### Option 1: Navigate to install URL to trigger app permission flow
```
http://127.0.0.1:8001/install
```
Note: you must change IP or port depending on your settings.

### Option 2: Run manual install to trigger app permission flow
```
python install.py
```
- Even if you use this manual version, you must run server.py to receive the callback!

## Send Bytes Web Form:
```
http://127.0.0.1:8001/send-bytes

# requires auth & server to be running!
```

## Send Bytes CLI:
```
python sendBytesCLI.py 1 5 Testin Python CLI for sendbytes

# format for CLI parameters: UID, Amount, Reason
```

## Send Bytes Script:
```
python sendBytestStatic.py

# uid, amount, and reason are set as variables in that file.
```


