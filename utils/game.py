def renderGame(gameName:str, gameId:int,  gameHash:int, layout:str):
    return """
    <svg xmlns="http://www.w3.org/2000/svg" width="200" height="100" version="1.1">
   <img/ src = http://media.steampowered.com/steamcommunity/public/images/apps/{}/{}.jpg >
   <text fill="##21130d" font-size="10" font-family="Verdana" x="0" y="0">{}</text>
   </svg>
    """.format(gameId, gameHash,gameName)

