import base64
import requests

def imgUrlToBase64DataImage(url):
    base64Strhash=  base64.b64encode(requests.get(url).content).decode('utf-8')
    dataImage = 'data:image/jpeg;charset=utf-8;base64,' + base64Strhash
    return dataImage

def sortOwnGames(data):
    res = sorted(data['games'], key=lambda x : x['playtime_forever'], reverse=True)
    return res

def replaceXmlCharacter(word):
    word = word.replace("<","&lt ")
    word = word.replace(">","&gt ")
    word = word.replace('"',"&quot; ")
    word = word.replace("&","and")
    print(word)
    return word