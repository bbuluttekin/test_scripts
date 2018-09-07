import requests

res = requests.get("http://www.nytimes.com")

print(res.headers)  # prints headers sent by server
