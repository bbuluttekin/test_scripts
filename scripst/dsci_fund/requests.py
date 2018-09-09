import requests

res = requests.get("http://www.nytimes.com")

print(res.headers)  # prints headers sent by server
print(res.status)  # status code of requests
print(res.ok)  # Boolean value to confirm status ok or not
