from utils.response import imgUrlToBase64DataImage


def renderUserCard(playerName: str, playerUrl: str, playerAvatarUrl: str, bgColor:str, textColor:str):
    dataImage = imgUrlToBase64DataImage(playerAvatarUrl)
    
    body =  """<svg xmlns="http://www.w3.org/2000/svg" width="150" height ="160" version="1.1">
          <rect x="0" y="0" rx="4.5" width="120" height="140" stroke="black" fill="{}" stroke-width="2"/>
          <image href="{}" x="10" y="10" height="100" width="100"/>
          <text x ='60' y ='130' text-anchor="middle" fill = "{}">{}</text>
          </svg>""".format(bgColor,dataImage,textColor,playerName)

    return body

def renderGame(gameName:str, gameId:int, gameTime:int, gameHash:int,x:int, y:int, width:int, height:int, layout:str):
    gameImgUrl = "http://media.steampowered.com/steamcommunity/public/images/apps/{}/{}.jpg".format(gameId,gameHash)
    dataImage = imgUrlToBase64DataImage(gameImgUrl)
    gameHours = round(gameTime/60,1)
    return """<svg xmlns="http://www.w3.org/2000/svg" x ="{x}" y="{y}" width="{width}" height ="{height}" version="1.1">
          <title>{gameName}</title>
          <rect  width="{width}" height="{height}" stroke="white" fill="transparent" stroke-width="2"/>
          <image x="10" y="0" href="{dataImg}"  height="100" width="100"/>
          <text x ='60' y ='90' text-anchor="middle" fill="black">{gameHours} hours</text>
          </svg>""".format(width=width, height=height, x=x, y=y, gameHours=gameHours, dataImg= dataImage,gameName=gameName)


def renderOwnedGamesCard(data, row:int, column:int):
    gameCards = ""
    totalWidth  = 120
    totalHeight = 0
    width = 120
    height = 100
    x = 0
    y = 0
    currentRow = 0
    currentCol = 0
    for game in data['topMostPlayedTenGames']:
        name = game['name']
        gid = game['appid']
        playTime = game['playtime_forever']
        logoHash = game['img_logo_url']
        gameCards += renderGame(name, gid, playTime, logoHash, x,y, width, height, 'full')
        if currentCol == 0:
            totalWidth += width
        if currentCol == column-1:
            y += height
            x = 0
            currentCol = 0
            currentRow += 1
            totalHeight += height
        elif currentRow != row:    
            x += width
            currentCol += 1
        elif currentRow == row:
            break

    return """<svg xmlns="http://www.w3.org/2000/svg"
      fill="none" width="{}" height="{}">
    {}</svg>""".format(totalWidth, totalHeight,gameCards)