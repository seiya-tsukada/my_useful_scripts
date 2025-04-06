# coding: utf-8

import requests
import json

token = "please set your token"
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={0}".format(token)
headers = {
    "Content-Type": "application/json"
}
data = {
    "contents": [{
        "parts": [{"text": "Explain how AI works"}]
    }]
}

response = requests.post(
    url,
    headers = headers,
    json = data
)

print(response)
print("Status:", response.status_code)
print("Response:", response.text)

