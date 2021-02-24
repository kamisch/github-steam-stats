# Github Steam Stats



# Demo

## Player's top most played game

![top played games list](https://githubsteamstats.herokuapp.com/api/getOwnedGames/76561198134424238?limit=6&boarderColor=purple&bgColor=purple&textColor=white)

copy and paste the following code to your github readme to list your top most played games from steam
```
![top played games list](https://githubsteamstats.herokuapp.com/api/getOwnedGames/<steam_id>)
```

## Player Profile

![steam profile](https://githubsteamstats.herokuapp.com/api/getPlayerSummaries/76561198134424238?boarderColor=white&boarderWidth=2&bgColor=282a36)

copy and paste the following code to your github readme to show your steam profile, other people can click your profile pic to checkout your steam profile. Use this on your own discretion
```
![steam profile](https://githubsteamstats.herokuapp.com/api/getPlayerSummaries/<steam_id>)
```

# Additional Parameters

steamId: str,
limit: Optional[int] = 6,
row: Optional[int] = 1,
col: Optional[int] = 12,
bgColor: Optional[str] = 'ffffff',
textColor: Optional[str] = '000000',
boarderColor: Optional[str] = '000000',
boarderWidth:  Optional[str] = '2'

# Deployment

This api is currently hosted on Heroku using the Heroku free tier dyno. 

# Steam Api
[![steam api](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Steam_logo.svg/320px-Steam_logo.svg.png)](https://developer.valvesoftware.com/wiki/Steam_Web_API)
