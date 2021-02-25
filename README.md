# Github Steam Stats



# Demo

## Player's top most played games Card

![top played games list](https://githubsteamstats.herokuapp.com/api/getOwnedGames/76561198134424238?limit=6&boarderColor=800080&bgColor=800080&textColor=ffffff)

copy and paste the following code to your github readme to list your top most played games from steam
```
![top played games list](https://githubsteamstats.herokuapp.com/api/getOwnedGames/<steam_id>)
```

## Player Profile Card

![steam profile](https://githubsteamstats.herokuapp.com/api/getPlayerSummaries/76561198134424238?boarderColor=white&boarderWidth=2&bgColor=282a36)

copy and paste the following code to your github readme to show your steam profile, other people can click your profile pic to checkout your steam profile. Use this on your own discretion
```
![steam profile](https://githubsteamstats.herokuapp.com/api/getPlayerSummaries/<steam_id>)
```
## Where to find your steam id

Open your steam client, and go to top right where you see your profile icon and your steam wallet ballance, click it and a dropdown should open. 
Click on Account Details, and you should see your steam id on the top left. 

# Additional Parameters

steamId: str,
limit: Optional[int] = 6,
row: Optional[int] = 1,
col: Optional[int] = 12,
bgColor: Optional[str] = 'ffffff',
textColor: Optional[str] = '000000',
boarderColor: Optional[str] = '000000',
boarderWidth:  Optional[str] = '2'

# Hosting

This api is currently hosted on Heroku using the Heroku free tier dyno. So that means if images of your cards didn't not showing up that might mean the heroku server was sleeping, try to refresh after a couple minutes.

# Development

This api is written with Fastapi, and it uses the Steam API to get all Steam related data. If you are interested in contributing to this project, please fork the repo and start a PR. 

# Steam Api Documentation
[![steam api](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Steam_logo.svg/320px-Steam_logo.svg.png)](https://developer.valvesoftware.com/wiki/Steam_Web_API)
