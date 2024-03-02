Run the server first, used to trade app permission token for access token
```
python server.py
```

Option 1: Navigate to install URL to trigger app permission flow
```
http://127.0.0.1:8001/install
```

Option 2: Run manual install to trigger app permission flow
```
python install.py
```

Access token is cached
- seen in tmp/accessToken file

Send Bytes Web Form:
```
http://127.0.0.1:8001/send-bytes
# requires auth & server to be running!
```

Send Bytes CLI:
```
python sendBytesCLI.py 1 5 Testin Python CLI for sendbytes
# format for CLI parameters: UID, Amount, Reason
```

Send Bytes Script:
```
python sendBytestStatic.py
# uid, amount, and reason are set as variables in that file.
```


