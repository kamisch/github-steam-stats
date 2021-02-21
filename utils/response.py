import base64
import requests

def imgUrlToBase64(url):
    return base64.b64encode(requests.get(url).content).decode('utf-8')

def sortOwnGames(data):
    res = sorted(data['games'], key=lambda x : x['playtime_forever'], reverse=True)
    return res