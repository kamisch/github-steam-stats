
def sortOwnGames(data):
    res = sorted(data['games'], key=lambda x : x['playtime_forever'], reverse=True)
    return res