def renderUserCard(playerName: str, playerUrl: str, playerAvatarUrl: str):
    body =  """<svg xmlns="http://www.w3.org/2000/svg" width="150" height ="160" version="1.1">
          <rect x="0" y="0" width="120" height="140" stroke="black" fill="transparent" stroke-width="2"/>
          <image href="{}" x="10" y="10" height="100" width="100"/>
          <text x ='60' y ='130' text-anchor="middle">{}</text>
          </svg>""".format(playerAvatarUrl,playerName)

    return body


def renderOwnedGamesCard(row, column):
    pass
