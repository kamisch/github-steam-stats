import requests 
import os
from utils.response import sortOwnGames
from dotenv import load_dotenv
load_dotenv()

apiKey = os.getenv('API_KEY')
async def getPlayerSummaries(steamid:str):
    url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={}&steamids={}".format(apiKey, steamid)
    response = requests.get(url)
    if response:
        print('Success!')
        data = response.json()
        res = {
            "playerName":  data['response']['players'][0]['personaname'],
            'playerProfileUrl': data['response']['players'][0]['profileurl'],
            'avatar': data['response']['players'][0]['avatarfull']
        }
        return res
    else:
        print('An error has occurred.')
    
async def getOwnedGames(steamid:str, limit:int):
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={}&steamid={}&format=json&include_appinfo=true&include_played_free_games=true".format(apiKey, steamid)
    response = requests.get(url)
    if response:
        print('Success!')
        data = response.json()
        sortedGames = sortOwnGames(data['response'])
        res = {
            "totalOwnedGames":  data['response']['game_count'],
            "topMostPlayedTenGames": sortedGames[:limit]
        }
        return res
    else:
        print('An error has occurred.')
