import requests

response = requests.get("https://www.google.com")

print(response.status_code) # return 200 if requests was succesful

print(response.text)