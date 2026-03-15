Install the Tool
Inside the project folder run:
```
pip install 403xKiech
```

To run the tool:
```
403x -u https://target.com/admin
```

To Run With Proxy:
Using Burp Suite:
```
403x -u https://target.com/admin -p http://127.0.0.1:8080
```
Run with custom payload list:
```
python3 403x.py -u https://target.com/admin -w payloads.txt
```
# But update the payload first in 403x/payload.txt
