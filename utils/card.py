from utils.response import imgUrlToBase64DataImage


def renderUserCard(playerName: str, playerUrl: str, playerAvatarUrl: str, bgColor:str, textColor:str):
    dataImage = imgUrlToBase64DataImage(playerAvatarUrl)
    
    body =  """<svg xmlns="http://www.w3.org/2000/svg" width="150" height ="160" version="1.1">
          <rect x="0" y="0" rx="4.5" width="120" height="140" stroke="black" fill="{}" stroke-width="2"/>
          <image href="{}" x="10" y="10" height="100" width="100"/>
          <text x ='60' y ='130' text-anchor="middle" fill = "{}">{}</text>
          </svg>""".format(bgColor,dataImage,textColor,playerName)

    return body

def renderGame(gameName:str, gameId:int, gameHash:int,x:int, y:int, layout:str):
    gameImgUrl = "http://media.steampowered.com/steamcommunity/public/images/apps/{}/{}.jpg".format(gameId,gameHash)
    dataImage = imgUrlToBase64DataImage(gameImgUrl)
    return """<svg class='gameCard' xmlns="http://www.w3.org/2000/svg" width="150" height ="160" version="1.1">
          <rect width="120" height="140" stroke="black" fill="transparent" stroke-width="2"/>
          <image href="{}" x="10" y="10" height="100" width="100"/>
          <text x ='60' y ='130' text-anchor="middle">{}</text>
          </svg>""".format(dataImage,gameName)


def renderOwnedGamesCard(data, row:int = 1, column:int=10):
    gameCards = ""
    for game in data['topMostPlayedTenGames']:
        name = game['name']
        gid = game['appid']
        playTime = game['playtime_forever']
        logoHash = game['img_logo_url']
        gameCards += renderGame(name, gid, logoHash, 'full')

    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1500 1600"
      fill="none">
    {}</svg>""".format(gameCards)