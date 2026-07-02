import requests

URL = "http://localhost:4499"

try:
    response = requests.get(URL, timeout=5)
    if response.status_code == 200:
        print("Application Status: UP")
    else:
        print("Application Status: DOWN")
except Exception as e:
    print("Application Status: DOWN")
    print(e)