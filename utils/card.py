def renderUserCard(playerName: str, playerUrl: str, playerAvatarUrl: str):
    body =  """<svg xmlns="http://www.w3.org/2000/svg" width="200" height="100" version="1.1">
          <img src = "{}" />
          <text x="50%" y="18" text-anchor="middle" font-family="Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji" font-weight="bold" font-size="13" fill="##21130d">{}</text>
          </svg>""".format(playerAvatarUrl,playerName)

    return body


def renderOwnedGamesCard(row, column):
    pass
