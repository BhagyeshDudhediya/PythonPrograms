import requests

response = requests.get('http://google.com')
print(response.status_code)
print(response.content)
print(response.headers)
#print(response.json())