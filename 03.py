import requests
import json

response = requests.get('http://data.phishtank.com/data/3f217296960694f7642692b73225c4cc332c627e719d19c7aab94787845905a2/online-valid.json.bz2')
print(response.status_code)
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

with open("C:\\Users\\DELL\\Downloads\\online.json", "r") as read_file:
    json.load(read_file)