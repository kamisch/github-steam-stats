from utils.response import imgUrlToBase64DataImage, replaceXmlCharacter


def renderUserCard(playerName: str, playerUrl: str, playerAvatarUrl: str,width:int, height:int, bgColor:str, textColor:str, borderColor:str, borderWidth:int):
    dataImage = imgUrlToBase64DataImage(playerAvatarUrl)
    playerName = replaceXmlCharacter(playerName)
    body =  """<svg xmlns="http://www.w3.org/2000/svg" width="150" height ="160" version="1.1">
          <rect x="0" y="0" rx="4.5" width="120" height="140" stroke="#{borderColor}" fill='#{bgColor}' stroke-width="{borderWidth}"/>
          <image href="{dataImage}" x="10" y="10" height="100" width="100"/>
          <text x ='60' y ='130' text-anchor="middle" font-family="Consolas, monospace" fill = "#{textColor}">{playerName}</text>
          </svg>""".format(playerName=playerName, playerUrl=playerUrl, dataImage=dataImage, bgColor=bgColor,textColor=textColor, borderColor=borderColor,borderWidth=borderWidth)

    return body

def renderGame(gameName:str, gameId:int, gameTime:int, gameHash:int,x:int, y:int, width:int, height:int, bgColor:str, textColor:str, borderColor:str, borderWidth:int):
    gameImgUrl = "http://media.steampowered.com/steamcommunity/public/images/apps/{}/{}.jpg".format(gameId,gameHash)
    dataImage = imgUrlToBase64DataImage(gameImgUrl)
    gameName = replaceXmlCharacter(gameName)
    gameHours = round(gameTime/60,1)
    body = """<svg xmlns="http://www.w3.org/2000/svg" x ="{x}" y="{y}" width="{width}" height ="{height}" version="1.1">
          <title>{gameName}</title>
          <rect  width="{width}" height="{height}" stroke="#{borderColor}" fill="#{bgColor}" stroke-width="{borderWidth}"/>
          <image x="10" y="0" href="{dataImg}"  height="50" width="100"/>
          <text x ='60' y ='60' text-anchor="middle" font-family="Consolas, monospace" fill="#{textColor}">{gameHours} hours</text>
          </svg>""".format(width=width, height=height, x=x, y=y, gameHours=gameHours, dataImg= dataImage,gameName=gameName,bgColor=bgColor,textColor=textColor, borderColor=borderColor,borderWidth=borderWidth)
    return body

def renderOwnedGamesCard(data, row:int, column:int,width:int, height:int, bgColor:str, textColor:str, borderColor:str, borderWidth:int):
    gameCards = ""
    totalWidth  = 120
    totalHeight = 0
    x = 0
    y = 0
    currentRow = 0
    currentCol = 0
    print("data", data)
    for game in data['topMostPlayedTenGames']:
        name = game['name']
        gid = game['appid']
        playTime = game['playtime_forever']
        logoHash = ''
        try:
            logoHash = game['img_logo_url']
        except:
            logoHash = game['img_icon_url']
        gameCards += renderGame(name, gid, playTime, logoHash, x,y, width, height, bgColor, textColor, borderColor, borderWidth)
        if currentRow == 0:
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